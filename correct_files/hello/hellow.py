# hellow.py: 最初のFlaskアプリ
from flask import Flask
from flask import render_template # 追加
from flask import request # 追加

app = Flask(__name__)

# トップ
@app.route('/')
def hellow_world():
    mojiretsu = 'ようこそ、Flaskの世界へ！'
    #print(mojiretsu)
    #return mojiretsu
    return render_template('index.html', mystr = mojiretsu) # 追加
