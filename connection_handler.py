import os
import sqlalchemy as db
from dataclasses import dataclass
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session


@dataclass(kw_only=True)
class ConnectionHandler:
    host: str = os.getenv('DB_HOST')
    user: str = os.getenv('DB_USER')
    password: str = os.getenv('DB_PASSWORD')
    database: str = os.getenv('DB_NAME')
    port: str = os.getenv('DB_PORT', '3306')  # Colocando um valor padrão, caso a variável de porta não exista
    conn: Engine = None
    session: Session = None

    def __post_init__(self):
        self.conn = db.create_engine(
            f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'
        )
        self.session = Session(bind=self.conn)
