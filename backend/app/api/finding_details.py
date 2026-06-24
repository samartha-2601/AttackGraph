from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.models.finding import Finding

router = APIRouter()


@router.get("/{finding_id}")
def get_finding(
    finding_id: int,
    db: Session = Depends(get_db)
):

    finding = (
        db.query(Finding)
        .filter(
            Finding.id == finding_id
        )
        .first()
    )

    return {
        "id": finding.id,
        "title": finding.title,
        "severity": finding.severity,
        "description": finding.description,
        "tool": finding.tool,
        "file_path": finding.file_path,
        "line_number": finding.line_number,

        "ai_exploitability":
            finding.ai_exploitability,

        "ai_confidence":
            finding.ai_confidence,

        "ai_remediation":
            finding.ai_remediation,

        "ai_attack_narrative":
            finding.ai_attack_narrative
    }