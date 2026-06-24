from app.services.ai.openai_service import (
    OpenAIService
)


class EnrichmentService:

    def enrich_finding(
        self,
        db,
        finding
    ):

        ai = OpenAIService()

        analysis = ai.triage_finding(
            finding
        )

        finding.ai_exploitability = (
            analysis.get(
                "exploitability",
                "Unknown"
            )
        )

        finding.ai_confidence = (
            analysis.get(
                "confidence",
                0
            )
        )

        finding.ai_remediation = (
            analysis.get(
                "remediation",
                ""
            )
        )

        finding.ai_attack_narrative = (
            analysis.get(
                "attack_narrative",
                ""
            )
        )

        db.commit()

        return analysis