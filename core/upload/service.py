from core.db import video


async def create_video(connection,**values):

    command = video.insert().values(values)
    await connection.execute(command)
