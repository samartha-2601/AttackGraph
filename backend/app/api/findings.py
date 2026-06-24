from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.models.finding import Finding

router = APIRouter()


@router.get("/")
def get_findings(
    db: Session = Depends(get_db)
):

    findings = db.query(Finding).all()

    response = []

    for f in findings:

        response.append(
            {
                "id": f.id,
                "title": f.title,
                "severity": f.severity,
                "tool": f.tool,
                "file_path": f.file_path,
                "line_number": f.line_number
            }
        )

    return response