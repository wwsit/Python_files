# *_*coding:utf-8

from kafka import KafkaProducer
import json

# pip install kafka-python
# 文档地址：https://cloud.tencent.com/document/product/597/63537

producer = KafkaProducer(
    bootstrap_servers=['ip地址:公网地址'],
    api_version=(1, 1),

    # SASL_PLAINTEXT 公网接入
    security_protocol="SASL_PLAINTEXT",
    sasl_mechanism="PLAIN",
    sasl_plain_username="用户名",
    sasl_plain_password="密码",
)

# 写入消息
for _ in range(10):
    message = "Hello World! Hello Ckafka!"
    msg = json.dumps(message, ensure_ascii=False).encode()

    # topic_test:topic名称
    producer.send('topic_test', value=msg)
    print("produce message " + message + " success.")

producer.close()
