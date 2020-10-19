from core.config.settings import DATABASES
from sqlalchemy import create_engine, MetaData
from core.db import video

db_config = DATABASES['native']

def get_engine(config=db_config):
    db_url = "postgresql://{user}:{password}@{host}:{port}/{database}".format(
        user=config['user'],
        password=config['password'],
        host=config['host'],
        port=config['port'],
        database=config['database']
    )

    engine = create_engine(db_url, isolation_level = "AUTOCOMMIT")
    return engine

def create_tables():
    engine = get_engine()

    meta = MetaData()
    meta.create_all(bind=engine, tables=[video])


if __name__ == '__main__':

    create_tables()
    print('CREATE ALL TABLES')
