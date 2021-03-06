import os
from aiohttp import web
from core.config.settings import MEDIA_URL
from .service import create_video
from core.db import video
from core.helpers import base_view


upload = web.RouteTableDef()

@upload.post('/upload/video')
@base_view
async def upload_video(request: web.Request) -> web.Response:
    try:
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

    except:
        return web.Response(text="Multipart is required")


    async with request.app['db'].acquire() as conn:
            await create_video(
                conn,
                user_id=1,
                video_description='Some',
                video_title="Title some video",
            )
    return web.Response(status = 200)
