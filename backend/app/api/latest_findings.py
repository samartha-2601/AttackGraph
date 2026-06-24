from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.models.scan import Scan
from app.models.finding import Finding

router = APIRouter()


@router.get("/")
def get_latest_findings(
    db: Session = Depends(get_db)
):

    latest_scan = (
        db.query(Scan)
        .order_by(Scan.id.desc())
        .first()
    )

    if not latest_scan:
        return []

    findings = (
        db.query(Finding)
        .filter(
            Finding.scan_id == latest_scan.id
        )
        .all()
    )

    response = []

    for finding in findings:

        response.append(
            {
                "id": finding.id,
                "title": finding.title,
                "severity": finding.severity,
                "tool": finding.tool,
                "file_path": finding.file_path,
                "line_number": finding.line_number
            }
        )

    return response