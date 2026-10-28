"""ProcedureCatalog implementation loading YAML procedure documents."""

import importlib.resources
import json
from dataclasses import dataclass
from typing import Any


class UnknownProcedureDocumentError(KeyError):
    """Raised when an unknown procedure document id is requested."""


@dataclass(frozen=True)
class ProcedureSummary:
    """Summary of a procedure document."""

    id: str
    code: str
    title: str
    kind: str
    uri: str


@dataclass(frozen=True)
class ProcedureDocument:
    """Full procedure document content and metadata."""

    id: str
    code: str
    title: str
    kind: str
    uri: str
    content: str


PROCEDURE_DEFINITIONS: list[dict[str, str]] = [
    {
        "id": "guide",
        "aliases": "guide,00-guide,00",
        "code": "GUIDE",
        "title": "Control Guide",
        "kind": "guide",
        "filename": "00-guide.yaml",
        "uri": "arale://procedure/guide",
    },
    {
        "id": "p01-project-reconnaissance",
        "aliases": "p01,01,01-project-reconnaissance",
        "code": "P01",
        "title": "Project Reconnaissance",
        "kind": "procedure",
        "filename": "01-project-reconnaissance.yaml",
        "uri": "arale://procedure/p01-project-reconnaissance",
    },
    {
        "id": "p02-initial-state-baseline",
        "aliases": "p02,02,02-initial-state-baseline",
        "code": "P02",
        "title": "Initial State Baseline",
        "kind": "procedure",
        "filename": "02-initial-state-baseline.yaml",
        "uri": "arale://procedure/p02-initial-state-baseline",
    },
    {
        "id": "p03-environment-diagnosis",
        "aliases": "p03,03,03-environment-diagnosis",
        "code": "P03",
        "title": "Environment Diagnosis",
        "kind": "procedure",
        "filename": "03-environment-diagnosis.yaml",
        "uri": "arale://procedure/p03-environment-diagnosis",
    },
    {
        "id": "p04-mandate-clarification",
        "aliases": "p04,04,04-mandate-clarification",
        "code": "P04",
        "title": "Mandate Clarification",
        "kind": "procedure",
        "filename": "04-mandate-clarification.yaml",
        "uri": "arale://procedure/p04-mandate-clarification",
    },
    {
        "id": "p05-behavior-specification",
        "aliases": "p05,05,05-behavior-specification",
        "code": "P05",
        "title": "Behavior Specification",
        "kind": "procedure",
        "filename": "05-behavior-specification.yaml",
        "uri": "arale://procedure/p05-behavior-specification",
    },
    {
        "id": "p06-interaction-design",
        "aliases": "p06,06,06-interaction-design",
        "code": "P06",
        "title": "Interaction Design",
        "kind": "procedure",
        "filename": "06-interaction-design.yaml",
        "uri": "arale://procedure/p06-interaction-design",
    },
    {
        "id": "p07-technical-design",
        "aliases": "p07,07,07-technical-design",
        "code": "P07",
        "title": "Technical Design",
        "kind": "procedure",
        "filename": "07-technical-design.yaml",
        "uri": "arale://procedure/p07-technical-design",
    },
    {
        "id": "p08-contracts-compatibility",
        "aliases": "p08,08,08-contracts-compatibility",
        "code": "P08",
        "title": "Contracts and Compatibility",
        "kind": "procedure",
        "filename": "08-contracts-compatibility.yaml",
        "uri": "arale://procedure/p08-contracts-compatibility",
    },
    {
        "id": "p09-plan-tasks-dependencies",
        "aliases": "p09,09,09-plan-tasks-dependencies",
        "code": "P09",
        "title": "Plan, Tasks and Dependencies",
        "kind": "procedure",
        "filename": "09-plan-tasks-dependencies.yaml",
        "uri": "arale://procedure/p09-plan-tasks-dependencies",
    },
    {
        "id": "p10-coherence-coverage",
        "aliases": "p10,10,10-coherence-coverage",
        "code": "P10",
        "title": "Coherence and Coverage",
        "kind": "procedure",
        "filename": "10-coherence-coverage.yaml",
        "uri": "arale://procedure/p10-coherence-coverage",
    },
    {
        "id": "p11-malfunction-diagnosis",
        "aliases": "p11,11,11-malfunction-diagnosis",
        "code": "P11",
        "title": "Malfunction Diagnosis",
        "kind": "procedure",
        "filename": "11-malfunction-diagnosis.yaml",
        "uri": "arale://procedure/p11-malfunction-diagnosis",
    },
    {
        "id": "p12-task-execution",
        "aliases": "p12,12,12-task-execution",
        "code": "P12",
        "title": "Task Execution",
        "kind": "procedure",
        "filename": "12-task-execution.yaml",
        "uri": "arale://procedure/p12-task-execution",
    },
    {
        "id": "p13-controlled-refactoring",
        "aliases": "p13,13,13-controlled-refactoring",
        "code": "P13",
        "title": "Controlled Refactoring",
        "kind": "procedure",
        "filename": "13-controlled-refactoring.yaml",
        "uri": "arale://procedure/p13-controlled-refactoring",
    },
    {
        "id": "p14-performance-optimization",
        "aliases": "p14,14,14-performance-optimization",
        "code": "P14",
        "title": "Performance and Optimization",
        "kind": "procedure",
        "filename": "14-performance-optimization.yaml",
        "uri": "arale://procedure/p14-performance-optimization",
    },
    {
        "id": "p15-testing-verification",
        "aliases": "p15,15,15-testing-verification",
        "code": "P15",
        "title": "Testing and Verification",
        "kind": "procedure",
        "filename": "15-testing-verification.yaml",
        "uri": "arale://procedure/p15-testing-verification",
    },
    {
        "id": "p16-change-review",
        "aliases": "p16,16,16-change-review",
        "code": "P16",
        "title": "Change Review",
        "kind": "procedure",
        "filename": "16-change-review.yaml",
        "uri": "arale://procedure/p16-change-review",
    },
    {
        "id": "p17-security-data-integrity",
        "aliases": "p17,17,17-security-data-integrity",
        "code": "P17",
        "title": "Security and Data Integrity",
        "kind": "procedure",
        "filename": "17-security-data-integrity.yaml",
        "uri": "arale://procedure/p17-security-data-integrity",
    },
    {
        "id": "p18-integration-migrations",
        "aliases": "p18,18,18-integration-migrations",
        "code": "P18",
        "title": "Integration and Migrations",
        "kind": "procedure",
        "filename": "18-integration-migrations.yaml",
        "uri": "arale://procedure/p18-integration-migrations",
    },
    {
        "id": "p19-state-recovery-replanning",
        "aliases": "p19,19,19-state-recovery-replanning",
        "code": "P19",
        "title": "State Recovery and Replanning",
        "kind": "procedure",
        "filename": "19-state-recovery-replanning.yaml",
        "uri": "arale://procedure/p19-state-recovery-replanning",
    },
    {
        "id": "p20-acceptance-delivery",
        "aliases": "p20,20,20-acceptance-delivery",
        "code": "P20",
        "title": "Acceptance and Delivery",
        "kind": "procedure",
        "filename": "20-acceptance-delivery.yaml",
        "uri": "arale://procedure/p20-acceptance-delivery",
    },
]


class ProcedureCatalog:
    """Catalog managing bundled Arale procedures."""

    def __init__(self) -> None:
        self._entries: list[ProcedureSummary] = []
        self._by_id: dict[str, dict[str, str]] = {}
        for item in PROCEDURE_DEFINITIONS:
            summary = ProcedureSummary(
                id=item["id"],
                code=item["code"],
                title=item["title"],
                kind=item["kind"],
                uri=item["uri"],
            )
            self._entries.append(summary)
            self._by_id[item["id"]] = item
            for alias in item["aliases"].split(","):
                if alias:
                    self._by_id[alias] = item

    def list_documents(self) -> list[ProcedureSummary]:
        """Return all procedure summaries in deterministic manifest order."""
        return list(self._entries)

    def list_ids(self) -> list[str]:
        """Return all canonical procedure IDs in manifest order."""
        return [item.id for item in self._entries]

    def get_document(self, id_or_alias: str) -> str:
        """Retrieve the exact raw YAML content for a procedure by ID or alias."""
        item = self._by_id.get(id_or_alias)
        if item is None:
            raise UnknownProcedureDocumentError(f"Unknown procedure id: {id_or_alias}")
        filename = item["filename"]
        resource_ref = importlib.resources.files("arale_code").joinpath("procedures", filename)
        return resource_ref.read_bytes().decode("utf-8")

    def to_json_manifest(self) -> str:
        """Serialize the catalog manifest to deterministic JSON string."""
        docs: list[dict[str, Any]] = [
            {
                "id": entry.id,
                "code": entry.code,
                "title": entry.title,
                "kind": entry.kind,
                "uri": entry.uri,
            }
            for entry in self._entries
        ]
        manifest = {
            "schema_version": 1,
            "documents": docs,
        }
        return json.dumps(manifest, separators=(",", ":"), ensure_ascii=False)
