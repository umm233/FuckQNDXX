#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, send_file
import requests as r
import os
import re

from genHead import make_head


def get_chinese(s):
    digit = {
        '0': '零',
        '1': '一',
        '2': '二',
        '3': '三',
        '4': '四',
        '5': '五',
        '6': '六',
        '7': '七',
        '8': '八',
        '9': '九'
    }
    return digit[s]


def download(pageUrl, s, e):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    down_path = "./static/img/qndxx/" + s + e + ".jpg"
    if os.path.isfile(down_path):
        pass
    else:
        re = r.get(pageUrl, headers=headers)
        if re.status_code == 200:
            with open(down_path, "wb+") as f:
                f.write(re.content)
        else:
            pass


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def fake_pic():
    s = str(request.form['s'])
    e = str(request.form['e'])
    pageUrl = str(request.form['pageUrl'])

    # 输入pageUrl，以下载对应图片
    if pageUrl:
        re_url = re.findall(r'(\w{10})', pageUrl)[0]
        se = re.findall(r'\d', re_url)
        s = se[0]
        e = se[1]

        # generate pic url and download
        url = "http://h5.cyol.com/special/daxuexi/" + re_url + r"/images/end.jpg"
        download(url, s, e)

    elif (s == "" or e == "" or (not (0 < int(s) < 20 and 0 < int(e) < 20))):
        return render_template('index.html', message="错误的查询范围。")

    down_img = "./static/img/qndxx/" + s + e + ".jpg"
    if os.path.isfile(down_img):
        make_head(down_img, get_chinese(s), get_chinese(e))
        return render_template('fake_pic.html',
                               pic_src='img/qndxx/latest.jpg',
                               s=get_chinese(s),
                               e=e)
    else:
        return render_template('404.html')


if __name__ == '__main__':
    # from waitress import serve
    # serve(app, host='0.0.0.0', port=5000)

    # 本地使用
    # app.run(host='127.0.0.1', port=5000, debug=True)

    # Docker部署使用
    app.run(host='0.0.0.0', port=5000, debug=True)
