import requests
import json
import queue
import threading

import redis
import random
import time
import signal
from retrying import retry
from functools import wraps


def run_timeout(time_out):
    def wrapper(fun):
        @wraps(fun)
        def func(*args, **kwargs):
            def handler(signum, frame):
                raise AssertionError
            try:
                signal.signal(signal.SIGALRM, handler)
                signal.alarm(time_out)
                return fun(*args, **kwargs)
            except AssertionError:
                print('timeout')
                return 'timeout'
        return func
    return wrapper


n = 0


@retry
@run_timeout(1)
def have_a_try():

    global n
    n += 1
    print('try {}'.format(n))
    time.sleep(1)
    if random.randint(0, 10) != 5:
        raise Exception('it is not 5')
    print('it is 5')



@run_timeout(5)
def t1():
    time.sleep(3)
    print('t1')
    return 't1'

from multiprocessing.pool import ThreadPool

