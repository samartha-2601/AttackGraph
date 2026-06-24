class AttackPathEngine:

    def generate_paths(
        self,
        categories
    ):

        paths = []

        if (
            "SQL Injection" in categories
            and
            "AWS Secret" in categories
        ):

            paths.append(
                {
                    "title":
                    "Potential Cloud Account Compromise",

                    "risk":
                    "HIGH",

                    "description":
                    "SQL Injection may expose AWS credentials which could enable cloud account abuse."
                }
            )

        if (
            "SQL Injection" in categories
            and
            "GitHub Token" in categories
        ):

            paths.append(
                {
                    "title":
                    "Potential Source Code Compromise",

                    "risk":
                    "HIGH",

                    "description":
                    "Database compromise could expose GitHub credentials leading to repository access."
                }
            )

        if (
            "GitHub Token" in categories
            and
            "API Key" in categories
        ):

            paths.append(
                {
                    "title":
                    "Potential Credential Abuse",

                    "risk":
                    "MEDIUM",

                    "description":
                    "Multiple exposed credentials increase risk of unauthorized access."
                }
            )

        return paths