import os

env = os.getenv('ENV')

if env == 'test':
    HOST = '123.56.14.5'
    PORT = 2181
    TOKEN = 'b0350c8c75ddcd99738df4c9346bec48dc9c4914'
elif env == 'prod':
    HOST = '123.56.14.5'
    PORT = 2181
    TOKEN = 'b0350c8c75ddcd99738df4c9346bec48dc9c4914'

else:
    HOST = '192.168.6.23'
    PORT = 9092
    TOKEN = 'b0350c8c75ddcd99738df4c9346bec48dc9c4914'