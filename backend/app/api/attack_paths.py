from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.models.finding import Finding

from app.services.correlation.correlator import (
    Correlator
)

from app.services.attack_paths.attack_path_engine import (
    AttackPathEngine
)

router = APIRouter()


@router.get("/")
def get_attack_paths(
    db: Session = Depends(get_db)
):

    findings = db.query(
        Finding
    ).all()

    correlator = Correlator()

    correlated = correlator.correlate(
        findings
    )

    categories = [
        item["category"]
        for item in correlated
    ]

    engine = AttackPathEngine()

    return engine.generate_paths(
        categories
    )