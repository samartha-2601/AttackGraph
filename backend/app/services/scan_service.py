from app.models.scan import Scan
from app.models.finding import Finding

from app.services.scanners.semgrep_scanner import SemgrepScanner
from app.services.scanners.gitleaks_scanner import GitleaksScanner


class ScanService:

    def save_findings(
        self,
        db,
        scan_id,
        findings
    ):

        for finding in findings:

            db_finding = Finding(
                scan_id=scan_id,
                title=finding["title"],
                severity=finding["severity"],
                description=finding["description"],
                confidence=finding["confidence"],
                tool=finding["tool"],
                file_path=finding["file_path"],
                line_number=finding["line_number"]
            )

            db.add(db_finding)

        db.commit()

    def run_all_scanners(
        self,
        db,
        target
    ):

        all_findings = []

        scanners = [
            SemgrepScanner(),
            GitleaksScanner()
        ]

        scan = Scan(
            project_id=1,
            tool="multi-scanner",
            status="completed"
        )

        db.add(scan)
        db.commit()
        db.refresh(scan)

        for scanner in scanners:

            results = scanner.scan(
                target
            )

            all_findings.extend(
                results
            )

        self.save_findings(
            db,
            scan.id,
            all_findings
        )

        return {
            "scan_id": scan.id,
            "findings": len(all_findings),
            "tools": [
                "semgrep",
                "gitleaks"
            ]
        }