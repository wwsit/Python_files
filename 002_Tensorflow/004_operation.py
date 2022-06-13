# -*-coding:utf-8-*-
import os
import tensorflow as tf

# 设置告警的级别
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 自定义图
new_g = tf.Graph()
with new_g.as_default():
    num11 = tf.constant(5)
    num22 = tf.constant(6, name="set_name")
    sum2 = num11 + num22

    # Tensor("Const:0", shape=(), dtype=int32)  Const:0-->指令名称
    print(num11)
    print(num22)
    print(sum2)
