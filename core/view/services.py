from core.db import video


async def view_all_videos(connection):


    cursor = await connection.execute(
        "SELECT * FROM video;"
    )

    records = await cursor.fetchall()
    videos = [dict(record) for record in records]

    return videos
