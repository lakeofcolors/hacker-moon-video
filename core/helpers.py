import functools
from aiohttp import web
import logging

logger = logging.getLogger(__name__)

def base_view(func):
    @functools.wraps(func)
    def wrapper(request,*args,**kwargs):

        try:
            logger.info("{} is running".format(func.__name__))
            return func(request,*args,**kwargs)
        except Exception as err:
            logger.error(err)
            return err

    return wrapper
