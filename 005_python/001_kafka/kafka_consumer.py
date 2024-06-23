# *_*coding:utf-8

from kafka import KafkaConsumer

# topic_test: topic名称
# group_test：消费组的名称
consumer = KafkaConsumer(
    'topic_test',
    group_id="group_test",
    bootstrap_servers=['ip地址:公网地址'],
    api_version=(1, 1),

    # SASL_PLAINTEXT 公网接入
    security_protocol="SASL_PLAINTEXT",
    sasl_mechanism="PLAIN",
    sasl_plain_username="用户名",
    sasl_plain_password="密码",
)

# 读取消息
for message in consumer:
    print(message)
    print("Topic:[%s] Partition:[%d] Offset:[%d] Value:[%s]" %
          (message.topic, message.partition, message.offset, message.value))
    print()
