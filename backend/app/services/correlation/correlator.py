class Correlator:

    def normalize_category(
        self,
        finding_title
    ):

        title = finding_title.lower()

        if "sql" in title:
            return "SQL Injection"

        if ("xss" in title or "format-string" in title):
            return "Cross Site Scripting"

        if "secret" in title:
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