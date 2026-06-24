from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.models.finding import Finding

from app.services.correlation.correlator import Correlator

router = APIRouter()


@router.get("/")
def correlate_findings(
    db: Session = Depends(get_db)
):

    findings = db.query(Finding).all()

    correlator = Correlator()

    results = correlator.correlate(
        findings
    )

    return results