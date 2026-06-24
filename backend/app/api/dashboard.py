from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.models.scan import Scan
from app.models.finding import Finding

router = APIRouter()


@router.get("/")
def dashboard(
    db: Session = Depends(get_db)
):

    scans = db.query(Scan).count()

    findings = db.query(Finding).count()

    sqli = (
        db.query(Finding)
        .filter(
            Finding.title.contains(
                "sql"
            )
        )
        .count()
    )

    xss = (
        db.query(Finding)
        .filter(
            Finding.title.contains(
                "format-string"
            )
        )
        .count()
    )

    return {
        "scans": scans,
        "findings": findings,
        "sql_injection": sqli,
        "xss": xss
    }