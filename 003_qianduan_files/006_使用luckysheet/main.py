# *_*coding:utf-8
import json
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

default_data = [
    {
        "name": "Sheet1",
        "color": "",
        "index": "index_1",
        "status": 1,
        "order": 0,
        "hide": 0,
        "row": 36,
        "column": 22,
        "defaultRowHeight": 10,
        "defaultColWidth": 80,
        "celldata": [
            {
                "r": 0,
                "c": 0,
                "v": {
                    "v": "标题",
                    "ct": {"fa": "General", "t": "g"},
                    "ff": "微软雅黑",
                    "fs": 16,
                    "bl": 1,
                    "m": "标题"
                }
            },
            {
                "r": 1,
                "c": 1,
                "v": 100
            },
            {
                "r": 1,
                "c": 2,
                "v": {
                    "v": "2024-01-18",
                    "ct": {"fa": "yyyy-MM-dd", "t": "d"},
                    "m": "2024-01-18"
                }
            },
            {
                "r": 2,
                "c": 0,
                "v": {
                    "v": "=SUM(B2:B10)",
                    "ct": {"fa": "General", "t": "g"},
                    "f": "=SUM(B2:B10)"
                }
            }
        ],
        "config": {
            "merge": {},
            "rowlen": {
                "0": 25,
                "1": 25,
                "2": 25
            }
        },

    },
    {
        "name": "Sheet2",
        "color": "",
        "index": "index_2",
        "status": 1,
        "order": 0,
        "hide": 0,
        "row": 36,
        "column": 22,
        "defaultRowHeight": 20,
        "defaultColWidth": 80,
        "celldata": [
            {
                "r": 0,
                "c": 0,
                "v": {
                    "v": "标题",
                    "ct": {"fa": "General", "t": "g"},
                    "ff": "微软雅黑",
                    "fs": 16,
                    "bl": 1,
                    "m": "标题"
                }
            },
            {
                "r": 1,
                "c": 1,
                "v": 100
            },
            {
                "r": 1,
                "c": 2,
                "v": {
                    "v": "2024-01-18",
                    "ct": {"fa": "yyyy-MM-dd", "t": "d"},
                    "m": "2024-01-18"
                }
            },
            {
                "r": 2,
                "c": 0,
                "v": {
                    "v": "=SUM(B2:B10)",
                    "ct": {"fa": "General", "t": "g"},
                    "f": "=SUM(B2:B10)"
                }
            }
        ],
        "config": {
            "merge": {},
            "rowlen": {}
        }
    },
]


@app.route("/", methods=["get"])
def test():
    return "ok"


@app.route("/luckysheet/initTabelData", methods=["post"])
def lucky_sheet_init_table_data():
    """初始化表格数据"""

    # 设置行高
    row_len_dict = {}
    for i in range(36):
        row_len_dict[str(i)] = 25
    default_data[0]["config"]["rowlen"] = row_len_dict

    # print(data[0]["config"]["rowlen"])

    return {"result": "success", "data": default_data}


@app.route("/luckysheet/updateTabelData", methods=["post"])
def lucky_sheet_update_table_data():
    """更新表格数据"""

    global default_data
    data_dict = json.loads(request.data)

    print(type(data_dict))
    default_data = data_dict["data"]

    return {"result": "success"}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6700, debug=True)

# eg:nohup python manager runserver 0.0.0.0:8000  >log.txt  2>&1  &

"""

nohup python3 main.py > ./log.txt 2<&1 &

"""
