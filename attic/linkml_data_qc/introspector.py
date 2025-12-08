"""Schema introspection utilities for identifying recommended slots."""

from dataclasses import dataclass, field

from linkml_runtime.utils.schemaview import SchemaView


@dataclass
class SlotInfo:
    """Information about a schema slot."""

    name: str
    range: str
    multivalued: bool
    recommended: bool
    inlined: bool


@dataclass
class ClassSlotMap:
    """Mapping of a class to its slots with recommended info."""

    class_name: str
    slots: list[SlotInfo] = field(default_factory=list)
    recommended_slots: list[str] = field(default_factory=list)


class SchemaIntrospector:
    """Analyze LinkML schema to identify recommended slots and traversal paths."""

    def __init__(self, schema_path: str):
        self.schema_path = schema_path
        self.sv = SchemaView(schema_path)
        self._recommended_cache: set[str] | None = None
        self._class_slot_cache: dict[str, ClassSlotMap] = {}

    @property
    def recommended_slots(self) -> set[str]:
        """Get all slot names marked as recommended."""
        if self._recommended_cache is None:
            self._recommended_cache = {
                s for s in self.sv.all_slots() if self.sv.get_slot(s).recommended
            }
        return self._recommended_cache

    def get_class_slots(self, class_name: str) -> ClassSlotMap:
        """Get slot information for a class."""
        if class_name in self._class_slot_cache:
            return self._class_slot_cache[class_name]

        slots = []
        for slot_name in self.sv.class_slots(class_name):
            slot = self.sv.get_slot(slot_name)
            slots.append(
                SlotInfo(
                    name=slot_name,
                    range=slot.range or "string",
                    multivalued=bool(slot.multivalued),
                    recommended=bool(slot.recommended),
                    inlined=bool(slot.inlined or slot.inlined_as_list),
                )
            )

        csm = ClassSlotMap(
            class_name=class_name,
            slots=slots,
            recommended_slots=[s.name for s in slots if s.recommended],
        )
        self._class_slot_cache[class_name] = csm
        return csm

    def is_class(self, name: str) -> bool:
        """Check if name refers to a defined class."""
        return name in self.sv.all_classes()

    def get_traversable_slots(self, class_name: str) -> list[SlotInfo]:
        """Get slots whose range is another class (for recursion)."""
        csm = self.get_class_slots(class_name)
        return [s for s in csm.slots if self.is_class(s.range) and s.inlined]
