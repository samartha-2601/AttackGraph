from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.models.finding import Finding

from app.services.ai.attack_path_ai import (
    AttackPathAI
)

router = APIRouter()


@router.get("/")
def generate_ai_attack_paths(
    db: Session = Depends(get_db)
):

    findings = db.query(
        Finding
    ).all()

    ai = AttackPathAI()

    return ai.generate(
        findings
    )