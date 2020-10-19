import os
from aiohttp import web
from core.config.settings import MEDIA_URL
from .service import create_video
from core.db import video

upload = web.RouteTableDef()

@upload.post('/upload/video')
async def upload_video(request: web.Request) -> web.Response:

    reader = await request.multipart()
    field = await reader.next()
    filename = field.filename

    size = 0
    with open(filename,'wb') as file:
        while True:
            chunk = await field.read_chunk()
            if not chunk:
                break
            size += len(chunk)
            file.write(chunk)


    async with request.app['db'].acquire() as conn:
        command = video.insert().values(user_id=1,video_title='New video',video_description='Description')
        await conn.execute(command)
    return web.Response(status = 200)
