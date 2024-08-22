from google.cloud import bigquery
from interfaces import IDatabaseStrategy

class BigQueryStrategy(IDatabaseStrategy):
    
    def __init__(self, project_id: str):
        self.project_id = project_id
        self.client = None

    def connect(self):
        try:
            self.client = bigquery.Client(project=self.project_id)
        except Exception as e:
            raise ConnectionError(f"Failed to connect to BigQuery: {e}")

    def get_all(self, table_id: str):
        try:
            query = f"SELECT * FROM `{table_id}`"
            results = self.client.query(query).result()
            return [dict(row) for row in results]
        except Exception as e:
            raise RuntimeError(f"Failed to retrieve data: {e}")

    def save(self, table_id: str, data: dict):
        try:
            table = self.client.get_table(table_id)
            errors = self.client.insert_rows_json(table, [data])
            if errors:
                raise RuntimeError(f"Errors occurred while inserting rows: {errors}")
        except Exception as e:
            raise RuntimeError(f"Failed to save data: {e}")

    def find_one(self, table_id: str, query: str):
        try:
            query_str = f"SELECT * FROM `{table_id}` WHERE {query}"
            results = self.client.query(query_str).result()
            return next(results, None)
        except Exception as e:
            raise RuntimeError(f"Failed to find data: {e}")
