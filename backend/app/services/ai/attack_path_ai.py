import json

from app.services.ai.openai_service import (
    OpenAIService
)


class AttackPathAI:

    def normalize_findings(
        self,
        findings
    ):

        normalized = []

        for finding in findings:

            title = finding.title.lower()

            if "sql" in title:
                normalized.append(
                    "SQL Injection"
                )

            elif "github" in title:
                normalized.append(
                    "GitHub Token"
                )

            elif "aws" in title:
                normalized.append(
                    "AWS Secret"
                )

            elif (
                "api key" in title
                or "generic api" in title
            ):
                normalized.append(
                    "API Key"
                )

            elif (
                "xss" in title
                or "format-string" in title
            ):
                normalized.append(
                    "Cross Site Scripting"
                )

        return list(
            set(normalized)
        )

    def generate(
        self,
        findings
    ):

        finding_titles = (
            self.normalize_findings(
                findings
            )
        )

        prompt = f"""
You are a senior application security architect.

Given these findings:

{finding_titles}

Generate realistic multi-step attack paths.

Focus on:

- attack chaining
- privilege escalation
- credential theft
- cloud compromise
- source code compromise
- business impact

Return ONLY valid JSON.

Schema:

{{
  "attack_paths": [
    {{
      "title": "string",

      "likelihood":
      "LOW|MEDIUM|HIGH",

      "impact":
      "LOW|MEDIUM|HIGH|CRITICAL",

      "priority":
      "P1|P2|P3|P4",

      "attack_chain": [
        "step"
      ],

      "mitre": [
        {{
          "id": "Txxxx",
          "name": "Technique Name"
        }}
      ]
    }}
  ]
}}
"""

        ai = OpenAIService()

        response = (
            ai.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                response_format={
                    "type": "json_object"
                }
            )
        )

        content = (
            response
            .choices[0]
            .message.content
        )

        result = json.loads(
            content
        )

        likelihood_map = {
            "LOW": 1,
            "MEDIUM": 2,
            "HIGH": 3
        }

        impact_map = {
            "LOW": 1,
            "MEDIUM": 2,
            "HIGH": 3,
            "CRITICAL": 4
        }

        for path in result[
            "attack_paths"
        ]:

            likelihood = (
                likelihood_map.get(
                    path[
                        "likelihood"
                    ].upper(),
                    1
                )
            )

            impact = (
                impact_map.get(
                    path[
                        "impact"
                    ].upper(),
                    1
                )
            )

            path[
                "risk_score"
            ] = (
                likelihood * impact
            )

        result[
            "attack_paths"
        ] = sorted(
            result[
                "attack_paths"
            ],
            key=lambda x:
            x["risk_score"],
            reverse=True
        )

        return result