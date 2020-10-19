from core.db import video

async def create_video(connection,user_id,video_title,video_description):
    command = vidoe.insert().values(user_id=user_id,video_title=video_title,video_description=video_description)
    await connection.execute(command)
