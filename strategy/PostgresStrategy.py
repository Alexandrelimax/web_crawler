from interfaces import IDatabaseStrategy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Table, MetaData

class PostgresStrategy(IDatabaseStrategy):
    
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.engine = create_engine(self.db_url)
        self.Session = sessionmaker(bind=self.engine)

    def connect(self):
        try:
            self.engine.connect()
        except Exception as e:
            raise ConnectionError(f"Failed to connect to the database: {e}")

    def get_all(self, table_name: str):
        try:
            session = self.Session()
            meta = MetaData(bind=self.engine)
            table = Table(table_name, meta, autoload_with=self.engine)
            result = session.query(table).all()
            session.close()
            return result
        except Exception as e:
            raise RuntimeError(f"Failed to retrieve data: {e}")

    def save(self, table_name: str, data: dict):
        try:
            session = self.Session()
            meta = MetaData(bind=self.engine)
            table = Table(table_name, meta, autoload_with=self.engine)
            insert_stmt = table.insert().values(**data)
            session.execute(insert_stmt)
            session.commit()
            session.close()
        except Exception as e:
            raise RuntimeError(f"Failed to save data: {e}")

    def find_one(self, table_name: str, query: dict):
        try:
            session = self.Session()
            meta = MetaData(bind=self.engine)
            table = Table(table_name, meta, autoload_with=self.engine)
            result = session.query(table).filter_by(**query).first()
            session.close()
            return result
        except Exception as e:
            raise RuntimeError(f"Failed to find data: {e}")
