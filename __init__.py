from aiohttp import web
from core.upload.routes import upload
from core.db import init_pg
from core.db import close_pg

async def make_app():
    app = web.Application()

    app.add_routes(upload)

    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)

    return app

if __name__ == '__main__':
    web.run_app(make_app())
