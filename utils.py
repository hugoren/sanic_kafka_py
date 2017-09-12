from functools import wraps
from sanic.response import json
from config import TOKEN


def auth(token):
    def wrapper(func):
        @wraps(func)
        async def auth_token(req, *arg, **kwargs):
            try:
                value = req.headers.get(token)
                if value and TOKEN == value:
                    r = await func(req, *arg, **kwargs)
                    return json({'retcode': 0, 'stdout': r})
                else:
                    return json({'retcode': 1, 'stderr': 'status{}'.format(403)})
            except Exception as e:
                return json({'retcode': 1, 'stderr': e})
        return auth_token
    return wrapper
