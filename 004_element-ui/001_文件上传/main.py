# -*- encoding: utf-8 -*-
import requests, os, json

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/api/saveData", methods=["post"])
def save_data():
    """保存数据"""
    try:

        files = request.files["files"]
        print(files)

        # 获取到文件的名称
        print(files.filename)

        # 保存数据
        files.save("./file/test.png")
        return {"result": "success"}
    except Exception as e:
        return {"result": "warn", "info": str(e)}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)