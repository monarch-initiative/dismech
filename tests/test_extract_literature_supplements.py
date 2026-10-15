"""Supplement transcription must preserve visible text and omit field code."""

import io
import zipfile

from scripts.extract_literature_supplements import extract_docx_text


def test_visible_runs_and_table_cells_keep_document_order():
    document = io.BytesIO()
    xml = """<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
    <w:body>
      <w:p><w:r><w:t>CRADD </w:t></w:r><w:r><w:t>p.Arg170His</w:t></w:r></w:p>
      <w:p><w:r><w:instrText>EN.CITE hidden database content</w:instrText></w:r>
        <w:r><w:t>Published citation 13</w:t></w:r></w:p>
      <w:tbl><w:tr><w:tc><w:p><w:r><w:t>FIN38</w:t></w:r></w:p></w:tc>
        <w:tc><w:p><w:r><w:t>Järvelä</w:t></w:r></w:p></w:tc></w:tr></w:tbl>
      <w:p/>
    </w:body></w:document>"""
    with zipfile.ZipFile(document, "w") as archive:
        archive.writestr("word/document.xml", xml)
    assert extract_docx_text(document.getvalue()) == (
        "CRADD p.Arg170His\n\nPublished citation 13\n\nFIN38\n\nJärvelä\n"
    )
