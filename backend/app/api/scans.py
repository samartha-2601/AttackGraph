from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.models.scan import Scan

from app.services.scan_service import ScanService

router = APIRouter()


@router.post("/run")
def run_scan(
    db: Session = Depends(get_db)
):

    service = ScanService()

    result = service.run_semgrep_scan(
        db,
        "../vulnerable-app"
    )

    return result


@router.get("/")
def get_scans(
    db: Session = Depends(get_db)
):
    scans = db.query(Scan).all()

    response = []

    for scan in scans:

        response.append(
            {
                "id": scan.id,
                "project_id": scan.project_id,
                "tool": scan.tool,
                "status": scan.status
            }
        )

    return response