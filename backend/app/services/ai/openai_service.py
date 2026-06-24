import os
import json

from openai import OpenAI


class OpenAIService:

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv(
                "OPENAI_API_KEY"
            )
        )

    def triage_finding(
        self,
        finding
    ):

        prompt = f"""
            Analyze this security finding.

            Return JSON only.

            {{
            "exploitability": "",
            "confidence": 0,
            "remediation": "",
            "attack_narrative": ""
            }}

            Title:
            {finding.title}

            Description:
            {finding.description}

            Severity:
            {finding.severity}
            """

        response = self.client.responses.create(
            model="gpt-5",
            input=prompt
        )

        

        try:
            return json.loads(
                response.output_text
            )
        except Exception:

            return {
                "exploitability": "Unknown",
                "confidence": 0,
                "remediation": "Unable to parse",
                "attack_narrative": ""
            }