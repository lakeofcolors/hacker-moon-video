from aiohttp import web
from core.upload.routes import upload
from core.view.routes import view
from core.db import init_pg
from core.db import close_pg
import logging
import aiohttp_cors


async def make_app():
    app = web.Application()

    app.add_routes(upload)
    app.add_routes(view)

    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)

    cors = aiohttp_cors.setup(app)

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(name)s - %(levelname)s - %(message)s',
    )

    return app

if __name__ == '__main__':
    web.run_app(make_app())
