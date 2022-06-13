# -*-coding:utf-8-*-
import os
import tensorflow as tf

# 设置告警的级别
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

num1 = tf.constant(5)
num2 = tf.constant(6)

sum1 = tf.add(num1, num2)

# 开启会话
with tf.Session() as sess:
    print(sess.run(sum1))

    # Tensorboard 可视化操作
    # 要保存的路径、要可视化的图
    # tf.summary.FileWriter("./tmp", graph=sess.graph)

    # 开启可视化，在终端输入
    # tensorboard --logdir="./tmp"
