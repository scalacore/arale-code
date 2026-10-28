"""InstructionCatalog implementation loading Markdown documents."""

import importlib.resources
import json
from dataclasses import dataclass
from typing import Any


class UnknownInstructionError(KeyError):
    """Raised when an unknown instruction document id is requested."""


@dataclass(frozen=True)
class InstructionSummary:
    """Summary of an engineering instruction document."""

    id: str
    title: str
    description: str
    priority: int
    uri: str


INSTRUCTION_DEFINITIONS: list[dict[str, Any]] = [
    {
        "id": "design-spec",
        "title": "Design specification",
        "description": "Defines the required system behavior and technical boundaries.",
        "priority": 100,
        "filename": "design-spec.md",
        "uri": "instructions://document/design-spec",
    },
    {
        "id": "implementation-plan",
        "title": "Implementation plan",
        "description": "Defines the ordered implementation tasks and acceptance checks.",
        "priority": 90,
        "filename": "implementation-plan.md",
        "uri": "instructions://document/implementation-plan",
    },
    {
        "id": "code-quality",
        "title": "Code quality rules",
        "description": "Defines coding, dependency, logging, and error-handling rules.",
        "priority": 80,
        "filename": "code-quality.md",
        "uri": "instructions://document/code-quality",
    },
    {
        "id": "testing",
        "title": "Testing rules",
        "description": "Defines the minimum test strategy and completion gates.",
        "priority": 70,
        "filename": "testing.md",
        "uri": "instructions://document/testing",
    },
]


class InstructionCatalog:
    """Catalog managing bundled Markdown engineering instructions."""

    def __init__(self) -> None:
        self._entries: list[InstructionSummary] = []
        self._by_id: dict[str, dict[str, Any]] = {}
        # Sorted strictly by descending priority, then ascending id
        sorted_defs = sorted(
            INSTRUCTION_DEFINITIONS,
            key=lambda item: (-int(item["priority"]), str(item["id"])),
        )
        for item in sorted_defs:
            summary = InstructionSummary(
                id=item["id"],
                title=item["title"],
                description=item["description"],
                priority=item["priority"],
                uri=item["uri"],
            )
            self._entries.append(summary)
            self._by_id[item["id"]] = item

    def list_documents(self) -> list[InstructionSummary]:
        """Return all instruction summaries sorted by descending priority."""
        return list(self._entries)

    def list_ids(self) -> list[str]:
        """Return all canonical instruction IDs."""
        return [item.id for item in self._entries]

    def get_document(self, id_: str) -> str:
        """Retrieve the exact raw Markdown content for an instruction by ID."""
        item = self._by_id.get(id_)
        if item is None:
            raise UnknownInstructionError(f"Unknown instruction id: {id_}")
        filename = item["filename"]
        resource_ref = importlib.resources.files("arale_code").joinpath("instructions", filename)
        return resource_ref.read_bytes().decode("utf-8")

    def to_json_manifest(self) -> str:
        """Serialize the catalog manifest to deterministic JSON string."""
        docs: list[dict[str, Any]] = [
            {
                "id": entry.id,
                "title": entry.title,
                "description": entry.description,
                "priority": entry.priority,
                "uri": entry.uri,
            }
            for entry in self._entries
        ]
        manifest = {
            "schema_version": 1,
            "documents": docs,
        }
        return json.dumps(manifest, separators=(",", ":"), ensure_ascii=False)
