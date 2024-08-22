from factory import DatabaseStrategyFactory, DatabaseContext

mongo_strategy = DatabaseStrategyFactory.create_strategy('mongo', mongo_url='mongodb://localhost:27017/', db_name='meu_banco_de_dados')
postgres_strategy = DatabaseStrategyFactory.create_strategy('postgres', db_url='postgresql://user:password@localhost/dbname')
bq_strategy = DatabaseStrategyFactory.create_strategy('bigquery', project_id='meu_projeto')


mongo_context = DatabaseContext(mongo_strategy)
postgres_context = DatabaseContext(postgres_strategy)
bq_context = DatabaseContext(bq_strategy)


mongo_context.connect()
postgres_context.connect()
bq_context.connect()