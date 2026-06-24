class Correlator:

    def normalize_category(
        self,
        finding_title
    ):

        title = finding_title.lower()

        # SQL Injection

        if (
            "sql" in title or
            "tainted-sql" in title
        ):
            return "SQL Injection"

        # XSS

        if (
            "xss" in title or
            "format-string" in title
        ):
            return "Cross Site Scripting"

        # GitHub

        if (
            "github" in title or
            "github token" in title or
            "github personal access token" in title
        ):
            return "GitHub Token"

        # AWS

        if (
            title == "aws" or
            "aws-access-token" in title
        ):
            return "AWS Secret"

        # API Keys

        if (
            "api key" in title or
            "generic-api-key" in title
        ):
            return "API Key"

        # Generic Secrets

        if (
            "secret" in title
        ):
            return "Hardcoded Secret"

        return "Other"

    def correlate(
        self,
        findings
    ):

        grouped = {}

        for finding in findings:

            category = self.normalize_category(
                finding.title
            )

            if category not in grouped:

                grouped[category] = {
                    "category": category,
                    "severity": finding.severity,
                    "count": 0,
                    "findings": []
                }

            grouped[category]["count"] += 1

            grouped[category]["findings"].append(
                finding.id
            )

        return list(grouped.values())