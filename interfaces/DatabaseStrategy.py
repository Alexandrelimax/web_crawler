from abc import ABC, abstractmethod

class IDatabaseStrategy(ABC):
    
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_all(self, table_name: str):
        pass

    @abstractmethod
    def save(self, table_name: str, data: dict):
        pass

    @abstractmethod
    def find_one(self, table_name: str, query: dict):
        pass
