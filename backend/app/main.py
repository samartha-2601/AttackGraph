from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

from app.api.projects import router as project_router
from app.db.init_db import init_db

from app.api.scans import router as scan_router
from app.api.findings import router as findings_router
from app.api.correlation import (
    router as correlation_router
)
from app.api.triage import (
    router as triage_router
)
from app.api.enrichment import (
    router as enrichment_router
)
from app.api.finding_details import (
    router as finding_details_router
)
from app.api.dashboard import (
    router as dashboard_router
)
from app.api.attack_paths import (
    router as attack_path_router
)

from app.api.latest_findings import (
    router as latest_findings_router
)

from app.api.ai_attack_paths import (
    router as ai_attack_path_router
)

app = FastAPI(
    title="AttackGraph AI"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

app.include_router(
    project_router,
    prefix="/projects",
    tags=["Projects"]
)

app.include_router(
    scan_router,
    prefix="/scans",
    tags=["Scans"]
)

app.include_router(
    findings_router,
    prefix="/findings",
    tags=["Findings"]
)

app.include_router(
    correlation_router,
    prefix="/correlation",
    tags=["Correlation"]
)

app.include_router(
    triage_router,
    prefix="/triage",
    tags=["AI Triage"]
)

app.include_router(
    enrichment_router,
    prefix="/enrichment",
    tags=["AI Enrichment"]
)

app.include_router(
    finding_details_router,
    prefix="/finding",
    tags=["Finding Details"]
)

app.include_router(
    dashboard_router,
    prefix="/dashboard",
    tags=["Dashboard"]
)

app.include_router(
    attack_path_router,
    prefix="/attack-paths",
    tags=["Attack Paths"]
)

app.include_router(
    latest_findings_router,
    prefix="/findings/latest",
    tags=["Latest Findings"]
)

app.include_router(
    ai_attack_path_router,
    prefix="/ai-attack-paths",
    tags=["AI Attack Paths"]
)


@app.get("/")
def root():
    return {
        "message": "AttackGraph AI API Running"
    }