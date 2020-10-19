import os

'''

Aiohttp settings for hacker-moon-video project

'''


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MEDIA_URL = os.path.join(os.path.dirname(BASE_DIR),'media','videos')

DATABASES = {
    'native': {
        'database': 'postgres',
        'user': 'postgres',
        'password': 'postgres',
        'host': 'db',
        'port': 5432,
        'minsize': 1,
        'maxsize': 5,
    },
}

HOST = "127.0.0.1"
PORT = 8080
