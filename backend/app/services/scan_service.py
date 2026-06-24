from app.models.scan import Scan
from app.models.finding import Finding

from app.services.scanners.semgrep_scanner import SemgrepScanner


class ScanService:

    def run_semgrep_scan(
        self,
        db,
        target
    ):

        scanner = SemgrepScanner()

        results = scanner.scan(target)

        scan = Scan(
            project_id=1,
            tool="semgrep",
            status="completed"
        )

        db.add(scan)
        db.commit()
        db.refresh(scan)

        for finding in results:

            db_finding = Finding(
                scan_id=scan.id,
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

        return scan.id, len(results)