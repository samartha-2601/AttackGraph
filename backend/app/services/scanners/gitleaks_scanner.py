import json
import subprocess

from app.services.scanners.base import BaseScanner


class GitleaksScanner(BaseScanner):

    def scan(self, target_path):

        command = [
            "gitleaks",
            "detect",
            "--source",
            target_path,
            "--no-git",
            "--report-format",
            "json",
            "--report-path",
            "gitleaks-report.json"
        ]

        try:

            subprocess.run(
                command,
                capture_output=True,
                text=True
            )

            with open(
                "gitleaks-report.json",
                "r"
            ) as f:

                raw_findings = json.load(f)

            findings = []

            for finding in raw_findings:

                findings.append(
                    {
                        "title": finding["Description"],
                        "severity": "ERROR",
                        "description": finding["RuleID"],
                        "confidence": "HIGH",
                        "tool": "gitleaks",
                        "file_path": finding["File"],
                        "line_number": finding["StartLine"]
                    }
                )

            return findings

        except Exception as e:

            print(e)

            return []