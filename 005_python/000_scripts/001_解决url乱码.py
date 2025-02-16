# # -*-coding:utf-8-*-
import requests


# 目标链接
url = "xxxx"

# 发送请求获取内容
response = requests.get(url)

# 尝试用不同编码解码内容
encodings = ['utf-8', 'gbk', 'latin-1']  # 常见的编码格式
for encoding in encodings:
    try:
        content = response.content.decode(encoding)
        print(f"成功解码（编码：{encoding}）：\n{content}")
        break
    except UnicodeDecodeError:
        continue
else:
    print("无法解码内容，可能是加密或压缩文件。")