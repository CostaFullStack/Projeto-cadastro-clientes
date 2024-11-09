import sqlalchemy as db
from dataclasses import dataclass
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session


@dataclass(kw_only=True)
class ConnectionHandler:
    host: str
    user: str
    password: str
    database: str
    port: str
    conn: Engine = None
    session: Session = None

    def __post_init__(self):
        self.conn = db.create_engine(
            f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'
        )
        self.session = Session(bind=self.conn)
