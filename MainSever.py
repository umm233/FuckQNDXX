from flask import Flask, request, render_template,send_file
import requests as r
import os

from genHead import make_head

def get_chinese(s):
    digit = {'0':'零','1':'一','2':'二','3':'三','4':'四','5':'五','6':'六','7':'七','8':'八','9':'九'}
    return digit[s]

def download(url,s,e):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    down_path = "./static/img/qndxx/"+s+e+".jpg"
    if not os.path.isfile(down_path):
        re=r.get(url, headers=headers)
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
    if (not (0<int(s)<20 or 0<int(e)<20)) or s=="" or e=="":
        return  render_template('index.html',message="错误的查询范围。")
    elif int(s)<3:
        return render_template('index.html',message="前两季暂时没有收录。")
    convert=['0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    url=r"http://h5.cyol.com/special/daxuexi/daxuexi"+s+convert[int(e)]+e+r"/images/end.jpg"
    print(url)
    download(url,s,e)

    down_img = "./static/img/qndxx/"+s+e+".jpg"
    make_head(down_img, get_chinese(s), get_chinese(e))
    return render_template('fake_pic.html', pic_src='img/qndxx/latest.jpg',s=get_chinese(s),e=e)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)
