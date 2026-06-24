from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.models.finding import Finding

from app.services.ai.enrichment_service import (
    EnrichmentService
)

router = APIRouter()


@router.post("/{finding_id}")
def enrich_finding(
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

    if not finding:

        return {
            "error": "Finding not found"
        }

    service = EnrichmentService()

    result = service.enrich_finding(
        db,
        finding
    )

    return result