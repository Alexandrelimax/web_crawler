from strategy import MongoStrategy, PostgresStrategy, BigQueryStrategy
from interfaces import IDatabaseStrategy
from typing import Type


class DatabaseStrategyFactory:
    _strategies: dict[str, Type[IDatabaseStrategy]] = {
        'mongo': MongoStrategy,
        'postgres': PostgresStrategy,
        'bigquery': BigQueryStrategy
    }

    @staticmethod
    def create_strategy(strategy_type: str, **kwargs) -> IDatabaseStrategy:
        strategy_class = DatabaseStrategyFactory._strategies.get(strategy_type)
        if not strategy_class:
            raise ValueError(f"Strategy type '{strategy_type}' is not recognized.")
        return strategy_class(**kwargs)
