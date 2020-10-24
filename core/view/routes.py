from aiohttp import web
from .services import view_all_videos


view = web.RouteTableDef()

@view.get('/view/index')
async def index(request: web.Request) -> web.json_response:

    async with request.app['db'].acquire() as conn:

        videos = await view_all_videos(conn)
        #async for row in conn.execute("SELECT * FROM video"):
        #     print(row.id,row.video_title)
        return web.json_response({'data':videos})
