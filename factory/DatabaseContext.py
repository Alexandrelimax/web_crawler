
class DatabaseContext:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def connect(self):
        self._strategy.connect()

    def get_all(self, table_name):
        return self._strategy.get_all(table_name)

    def save(self, table_name, data):
        self._strategy.save(table_name, data)

    def find_one(self, table_name, query):
        return self._strategy.find_one(table_name, query)
