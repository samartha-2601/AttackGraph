from app.services.scanners.base import BaseScanner


class MockScanner(BaseScanner):

    def scan(self, target):

        return [
            {
                "title": "SQL Injection",
                "severity": "High",
                "description": "Unsanitized user input in login endpoint",
                "confidence": 95
            },
            {
                "title": "Hardcoded Secret",
                "severity": "Medium",
                "description": "API key found in source code",
                "confidence": 88
            }
        ]