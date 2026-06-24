from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Float

from app.db.database import Base


class Finding(Base):
    __tablename__ = "findings"

    id = Column(Integer, primary_key=True, index=True)

    scan_id = Column(
        Integer,
        ForeignKey("scans.id")
    )

    title = Column(String)

    severity = Column(String)

    description = Column(String)

    confidence = Column(Integer)

    tool = Column(String)

    file_path = Column(String)

    line_number = Column(Integer)

    ai_exploitability = Column(String)

    ai_confidence = Column(Float)

    ai_remediation = Column(String)

    ai_attack_narrative = Column(String)