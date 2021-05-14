# input.py: フォーム入力の出力
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

# トップ
@app.route('/', methods = ['GET', 'POST']) # POSTのみ入力に
def show_input():
    input = '入力なし'
    if request.method == 'POST':
        input = request.form['form_input'] # <input name="form_input" ...>

    return render_template('index.html', mystr = input)
