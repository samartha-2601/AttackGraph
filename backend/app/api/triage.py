from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.models.finding import Finding

from app.services.ai.openai_service import (
    OpenAIService
)

router = APIRouter()


@router.get("/{finding_id}")
def triage_finding(
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

    ai = OpenAIService()

    result = ai.triage_finding(
        finding
    )

    return {
        "finding_id": finding_id,
        "analysis": result
    }