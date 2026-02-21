#!/usr/bin/env python3
"""
PreToolUse hook to validate kb/disorders/*.yaml files BEFORE edits are applied.

This hook:
1. Intercepts Edit/Write/MultiEdit calls targeting kb/disorders/*.yaml
2. Simulates what the file would look like after the edit
3. Runs `just validate <temp_file>` on the simulated result
4. Returns exit code 2 to BLOCK the edit if validation fails

Exit code 2 blocks the operation in PreToolUse hooks.
https://docs.claude.com/en/docs/claude-code/hooks#exit-code-2-behavior
"""

import sys
import json
import subprocess
import tempfile
from pathlib import Path


def simulate_edit(file_path: Path, old_string: str, new_string: str) -> str:
    """Simulate an Edit operation and return the resulting content."""
    if not file_path.exists():
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(0)  # Let Claude Code handle missing file error

    content = file_path.read_text()

    # Check if old_string exists in file
    if old_string not in content:
        print("Error: old_string not found in file", file=sys.stderr)
        sys.exit(0)  # Let Claude Code handle this error

    # Perform the replacement
    return content.replace(old_string, new_string, 1)


def simulate_write(content: str) -> str:
    """Simulate a Write operation - just return the new content."""
    return content


def simulate_multi_edit(file_path: Path, edits: list) -> str:
    """Simulate a MultiEdit operation and return the resulting content."""
    if not file_path.exists():
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(0)

    content = file_path.read_text()

    for edit in edits:
        old_string = edit.get("old_string", "")
        new_string = edit.get("new_string", "")
        if old_string and old_string in content:
            content = content.replace(old_string, new_string, 1)

    return content


def validate_content(
    content: str, original_path: Path, project_root: Path
) -> tuple[bool, str]:
    """
    Validate content by writing to temp file and running validation.
    Returns (success, output_message).
    """
    # Create temp file with same name in temp directory
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_path = Path(tmpdir) / original_path.name
        temp_path.write_text(content)

        # Run validation command
        cmd = ["just", "validate", str(temp_path)]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=project_root,
        )

        output = result.stdout + result.stderr
        return result.returncode == 0, output


def main():
    # Read the hook input from stdin
    data = json.load(sys.stdin)

    tool_name = data.get("tool_name", "")
    tool_input = data.get("tool_input", {})

    # Only process Write, Edit, and MultiEdit tool calls
    if tool_name not in ["Write", "Edit", "MultiEdit"]:
        sys.exit(0)

    file_path_str = tool_input.get("file_path", "")
    if not file_path_str:
        sys.exit(0)

    file_path = Path(file_path_str)

    # Check if it's in kb/disorders/ and is a .yaml file
    if "kb/disorders" not in str(file_path) or file_path.suffix != ".yaml":
        sys.exit(0)

    # Determine project root (go up from .claude/hooks/)
    project_root = Path(__file__).parent.parent.parent

    # Simulate the edit to get resulting content
    if tool_name == "Edit":
        old_string = tool_input.get("old_string", "")
        new_string = tool_input.get("new_string", "")
        simulated_content = simulate_edit(file_path, old_string, new_string)
    elif tool_name == "Write":
        simulated_content = simulate_write(tool_input.get("content", ""))
    elif tool_name == "MultiEdit":
        edits = tool_input.get("edits", [])
        simulated_content = simulate_multi_edit(file_path, edits)
    else:
        sys.exit(0)

    # Validate the simulated content
    success, output = validate_content(simulated_content, file_path, project_root)

    # Display results
    print("\n" + "=" * 60, file=sys.stderr)
    print(f"Pre-Edit Validation for {file_path.name}", file=sys.stderr)
    print("=" * 60, file=sys.stderr)

    if output.strip():
        print(output.strip(), file=sys.stderr)

    if not success:
        print("=" * 60, file=sys.stderr)
        print("❌ BLOCKING EDIT: Validation failed", file=sys.stderr)
        print("The proposed edit would create an invalid file.", file=sys.stderr)
        print("Fix the issues above before proceeding.", file=sys.stderr)
        print("=" * 60 + "\n", file=sys.stderr)
        sys.exit(2)  # Block the operation

    print("✓ Validation passed - allowing edit", file=sys.stderr)
    print("=" * 60 + "\n", file=sys.stderr)
    sys.exit(0)


if __name__ == "__main__":
    main()
