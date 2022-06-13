# -*-coding:utf-8-*-
import os
import math
import time
import json
import js2py
import requests
from urllib import parse, request


class KuGouSpider(object):

    def __init__(self, name):
        self.name = name
        self.start_flag = 1
        self.end_flag = 10
        self.recent_page = 1
        self.url = ""
        self.list_data = []

    def fun(self, blocknum, bs, size):
        """显示下载的进度"""

        percent = blocknum * bs / size
        percent = percent * 100
        int_data = int(percent)
        if int_data % 20 == 0:
            if int_data not in self.list_data:
                print("download: %d%%" % (int_data))
                self.list_data.append(int_data)

    def save_song(self, lyrics_cotent, items, url):
        """保存歌词和下载音频"""

        self.list_data = []
        print("正在下载的内容:"+ items['SingerName'] + '-' + items['song_name'])
        file_path = './music'
        path = './music/' + items['SingerName'] + '-' + items['song_name'] + '.txt'
        print('文件路径:%s' % os.getcwd() + '\\music')

        if not os.path.exists(file_path):
            os.mkdir('./music')
        # 保存歌词
        with open(path, 'w+', encoding='utf-8') as f:
            f.write(lyrics_cotent + '\n')
        # 下载音频
        request.urlretrieve(url=url, filename='./music/' + items['SingerName'] + '-' + items['song_name'] + '.mp3',
                            reporthook=self.fun)

    def execute_js(self):
        """获取url地址"""

        # 获取毫秒的时间戳
        time_result = time.time() * 1000
        context = js2py.EvalJs()
        js_time = round(time_result)


        signature_value = "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtbitrate=0callback=callback123clienttime=%sclientver=2000dfid" \
                          "=-inputtype=0iscorrection=1isfuzzy=0keyword=%smid=%spage=1pagesize=30platform" \
                          "=WebFilterprivilege_filter=0srcappid=2919tag=emuserid=-1uuid=%sNVPh5oo715z5DIWAeQlhMDsWXXQV4hwt" \
                          % (
                              js_time, self.name, js_time, js_time)

        with open('./kugou.js', 'r', encoding='utf-8') as f:
            context.execute(f.read())
        # 执行JS代码，获取signature值
        result = context.faultylabs.MD5(signature_value)

        # 进行字符串编码
        parser_name = parse.quote(self.name)

        # 获取url(获取搜索列表)
        self.url = "https://complexsearch.kugou.com/v2/search/song?callback=callback123&keyword=%s&page=1&pagesize=30" \
                   "&bitrate=0&isfuzzy=0&tag=em&inputtype=0&platform=WebFilter&userid=-1&clientver=2000&iscorrection" \
                   "=1&privilege_filter=0&srcappid=2919&clienttime=%s&mid=%s&uuid=%s&dfid=-&signature=%s" % (
                       parser_name, js_time, js_time, js_time, result)

    def get_response(self):
        """获取响应内容"""

        resp = requests.get(self.url)
        result = resp.text

        # 去掉左右括号,转成字典类型
        result_str = result[12:-2]
        result_dict = json.loads(result_str)
        result_dict = result_dict["data"]["lists"]

        # 向上取整数
        page_num = math.ceil(len(result_dict) / 10)

        down_item_list = []
        while True:
            i = 0

            for single_content in result_dict:

                items = {}
                items["AlbumID"] = single_content['AlbumID']
                # 专辑
                items["AlbumName"] = single_content['AlbumName']
                # 歌曲名
                items["song_name"] = single_content['SongName'].replace('<em>', '').replace('</em>', '')
                # 歌手
                items["SingerName"] = single_content['SingerName'].replace('<em>', '').replace('</em>', '')
                # 普通音质
                items["FileHash"] = single_content['FileHash']
                # HQF音质
                items["HQFileHash"] = single_content['HQFileHash']

                down_item_list.append(items)

                i += 1
                if self.start_flag <= i <= self.end_flag:
                    print(
                        '序号:%s  歌手:%s  歌名:%s  专辑:%s' % (i, items["SingerName"], items["song_name"], items["AlbumName"]))

            if self.display_page(page_num, down_item_list):
                break
            print()

    def display_page(self, page_num, down_item_list):
        """展示内容"""

        #  当前是第一页
        if self.recent_page == 1:
            input_content = input('共%s页，当前是第1页,下载音频(输入:d),下一页(请输入:n),返回(输入b):' % page_num)
            if input_content.lower() == 'n':
                self.start_flag = 11
                self.end_flag = 20
                self.recent_page = 2
            elif input_content.lower() == 'd':
                down_num = input('请输入需要下载歌词的序号，0代表全部:')
                if 1 <= int(down_num) <= 10:
                    self.get_page_response(down_item_list[int(down_num)])
                elif int(down_num) == 0:
                    self.get_page_response(down_item_list[:10])
                else:
                    print('输入有误,请输入1--10之间的数字')
            elif input_content.lower() == 'b':
                print()
                return True

        else:
            # 不是第一页
            input_content = input(
                '共%s页，当前是第%s页,下载音频(输入:d),上一页(请输入:u),下一页(请输入:n),返回(输入b):' % (page_num, self.recent_page))
            if input_content.lower() == 'u':

                self.start_flag = self.start_flag - 10
                self.end_flag = self.end_flag - 10
                self.recent_page = self.recent_page - 1

            elif self.recent_page == page_num:

                if input_content.lower() == 'd':
                    down_num = input('请输入需要下载歌词的序号，0代表全部:')
                    if self.start_flag <= int(down_num) <= self.end_flag:
                        self.get_page_response(down_item_list[int(down_num)])
                    elif int(down_num) == 0:
                        self.get_page_response(down_item_list[self.start_flag-1:self.end_flag])
                    else:
                        print('输入有误,请输入%s--%s之间的数字' % (self.start_flag, self.end_flag))

            elif input_content.lower() == 'n':
                self.start_flag = 10 * self.recent_page + 1
                self.end_flag = 10 * self.recent_page + 10
                self.recent_page = self.recent_page + 1

            elif input_content.lower() == 'd':

                down_num = input('请输入需要下载歌词的序号，0代表全部:')
                if self.start_flag <= int(down_num) <= self.end_flag:
                    self.get_page_response(down_item_list[int(down_num)])
                elif int(down_num) == 0:
                    self.get_page_response(down_item_list[self.start_flag - 1:self.end_flag])
                else:
                    print('输入有误,请输入%s--%s之间的数字' % (self.start_flag, self.end_flag))

            elif input_content.lower() == 'b':
                return True

    def get_page_response(self, items):
        """进入歌曲页面"""

        # 只下载一首歌
        if len(items) == 6:
            # 歌曲页面的url
            song_url = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash=%s&album_id=%s&dfid=07uEDT2bAFsd0uOUa529rw1t&mid=baf581192a4beeb14d5a1c6934a6acfb' % (
                items['FileHash'], items['AlbumID'])

            resp = requests.get(song_url).text
            # unicode编码转换成中文
            resp = resp.encode('utf8').decode('unicode_escape')

            # 歌词
            lyrics_cotent = resp[resp.find('lyrics') + 9:resp.find('author_id') - 3]

            resp_str = '{"' + resp[resp.find('play_url":'):-1]
            # 转成字典
            resp_dict = json.loads(resp_str)
            # 音频地址
            down_music_url = resp_dict['play_url']
            print(down_music_url)

            self.save_song(lyrics_cotent, items, down_music_url)

        # 下载所有歌
        elif len(items) >1:
            for item in items:
                # 歌曲页面的url
                song_url = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash=%s&album_id=%s&dfid=07uEDT2bAFsd0uOUa529rw1t&mid=baf581192a4beeb14d5a1c6934a6acfb' % (
                    item['FileHash'], item['AlbumID'])

                resp = requests.get(song_url).text
                # unicode编码转换成中文
                resp = resp.encode('utf8').decode('unicode_escape')

                # 歌词
                lyrics_cotent = resp[resp.find('lyrics') + 9:resp.find('author_id') - 3]

                resp_str = '{"' + resp[resp.find('play_url":'):-1]
                # 转成字典
                resp_dict = json.loads(resp_str)
                # 音频地址
                down_music_url = resp_dict['play_url']
                print(down_music_url)

                self.save_song(lyrics_cotent, item, down_music_url)
                time.sleep(5)

    def run(self):

        self.execute_js()
        self.get_response()


if __name__ == '__main__':
    while True:
        name = input('请输入歌手/歌名:')
        if name == 'y':
            break
        user = KuGouSpider(name)
        user.run()
        print('结束程序请输入:y')
