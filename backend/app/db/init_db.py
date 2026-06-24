from app.db.database import engine
from app.db.database import Base

from app.models.project import Project
from app.models.scan import Scan
from app.models.finding import Finding


def init_db():
    Base.metadata.create_all(bind=engine)