import sqlalchemy as sa
from aiopg.sa import create_engine
from core.config.settings import DATABASES

meta = sa.MetaData()

video = sa.Table(
    'video', meta,
    sa.Column('id', sa.Integer, nullable=False, primary_key=True),
    sa.Column('video_title', sa.String(255), nullable=False),
    sa.Column('video_description', sa.String(255), nullable=False),
    sa.Column('user_id', sa.Integer, nullable=False)
)



async def init_pg(app):
    config = DATABASES['native']
    engine = await create_engine(
        database = config['database'],
        user = config['user'],
        password = config['password'],
        host = config['host'],
        port = config['port'],
        minsize = config['minsize'],
        maxsize = config['maxsize'],
    )
    app['db'] = engine

async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()
