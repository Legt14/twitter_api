from sqlalchemy import create_engine, MetaData

engine = create_engine('postgresql+psycopg2://postgres:admin@localhost:5432/twitter_api')

meta = MetaData()

conn = engine.connect()
