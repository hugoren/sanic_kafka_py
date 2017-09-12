# kafka 客户端
http://kafka-python.readthedocs.io/en/master/index.html

## 注意点

1.kafka服务端设置
server.properties
listeners=PLAINTEXT://192.168.6.23:9092(否则生产者发送不了数据)

2.kafka客户端消费数据设置groud_id, 否则获取不到消费者数据
 consumer = KafkaConsumer('t3',group_id='my_favorite_group',bootstrap_servers=['{0}:{1}'.format(HOST, PORT)],

