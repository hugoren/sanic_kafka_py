import asyncio
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError
from config import HOST, PORT


async def kafka_producer():
    producer = KafkaProducer(bootstrap_servers=['{0}:{1}'.format(HOST, PORT)], api_version=(0, 10))
    try:
        for _ in range(1000):
            future = producer.send('t3', b'hugo hello')
        producer.flush()
        record_metadata = future.get(timeout=5)
        print(record_metadata)
    except KafkaError as e:
        print(e)


def kafka_consumer():
    consumer = KafkaConsumer('t3',group_id='my_favorite_group',bootstrap_servers=['{0}:{1}'.format(HOST, PORT)],

                             )
    for message in consumer:
        print(message)
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
        print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                             message.offset, message.key,
                                             message.value))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(kafka_producer())
#     loop.run_until_complete(kafka_consumer())

kafka_consumer()

