# -*-coding:utf-8-*-
import os
import tensorflow as tf

# 设置告警的级别
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

num1 = tf.constant(5)
num2 = tf.constant(6)

sum1 = tf.add(num1, num2)

# 查看默认图
default_g = tf.get_default_graph()
print("默认图:%s" % default_g)

# 查看属性
print(num1.graph)
print(num2.graph)

# 开启会话
with tf.Session() as sess:
    value = sess.run(sum1)
    print(value)
    print("sess的图属性:%s" % sess.graph)

print()

# 自定义图
new_g = tf.Graph()

# 开启会话
with new_g.as_default():
    num11 = tf.constant(5)
    num22 = tf.constant(6)
    sum2 = num11 + num22
    print(sum2)
    print(num11.graph)
    print(num22.graph)
