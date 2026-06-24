import json
import subprocess

from app.services.scanners.base import BaseScanner


class SemgrepScanner(BaseScanner):

    def scan(self, target):

        command = [
            "semgrep",
            "scan",
            target,
            "--config",
            "auto",
            "--json"
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        data = json.loads(result.stdout)

        findings = []

        for item in data["results"]:

            findings.append(
                {
                    "title": item["check_id"],
                    "severity": item["extra"]["severity"],
                    "description": item["extra"]["message"],
                    "file_path": item["path"],
                    "line_number": item["start"]["line"],
                    "tool": "semgrep",
                    "confidence": 90
                }
            )

        return findings