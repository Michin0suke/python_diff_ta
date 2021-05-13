import os
import difflib

tree = [
  # 1
    [
      {
        'type': 'file',
        'name': 'hellow.py',
        'content': '''# hellow.py: 最初のFlaskアプリ
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
'''.splitlines(keepends=True),
      },
      {
        'type': 'directory',
        'name': 'templates',
        'files': [
          {
            'type': 'file',
            'name': 'index.html',
            'content': '''{# index.html #}
{% extends 'template.html' %}
{% block main_content %}
<!-- 文字列を挿入 -->
{{mystr}}
{% endblock %}
'''.splitlines(keepends=True),
          },
          {
            'type': 'file',
            'name': 'template.html',
            'content': '''<!DOCTYPE html>
<html>
    <header>
        <meta charset="UTF-8" />
        <title>First Flask Application by ---</title>
    <body>
        <h1>最初のFlaskアプリケーション</h1>
        <h2>---</h2>
        <hr />
        {% block main_content %}
        {% endblock %}
        <hr />
        <address>Copyright (c) 2021 ---</address>
    </body>
</html>
'''.splitlines(keepends=True),
          },
        ],
      },
    ],


    # 2
    [
      {
        'type': 'file',
        'name': 'input.py',
        'content': '''# input.py: フォーム入力の出力
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
'''.splitlines(keepends=True),
      },
      {
        'type': 'directory',
        'name': 'templates',
        'files': [
          {
            'type': 'file',
            'name': 'index.html',
            'content': '''{# index.html #}
{% extends 'template.html' %}
{% block main_content %}
<form method="POST">
    <p>入力文字列: <input type="text" name="form_input" size="30" /></p>
    <p>
        <input type="submit" value="入力確定" />
        <input type="reset" value="消去" />
    </p>
</form>
<!-- 入力があれば文字列を挿入-->
<p>入力文字列:  {{mystr}}</p>
{% endblock %}
'''.splitlines(keepends=True),
          },
          {
            'type': 'file',
            'name': 'template.html',
            'content': '''<!DOCTYPE html>
<html>
    <header>
        <meta charset="UTF-8" />
        <title> Second Flask Application by ---</title>
    <body>
        <h1>フォームの入力の出力</h1>
        <h2>---</h2>
        <hr/>
        {% block main_content %}
        {% endblock %}
        <hr />
        <address>Copyright (c) 2021 ---</address>
    </body>
</html>
'''.splitlines(keepends=True),
          },
        ],
      },
    ],

    # 3
    [
      {
        'type': 'file',
        'name': 'address.py',
        'content': '''# address.py: 住所録アプリ
from flask import Flask, render_template, request, redirect, url_for
import sqlite3 # SQLite3パッケージ

DATABASE_NAME = 'address.db'
app = Flask(__name__)


# [ヘルパ関数] SQLを実行する
def execute_sql(sql):
    con = sqlite3.connect(DATABASE_NAME)
    cur = con.cursor()
    result = []

    for row in cur.execute(sql):
        result.append(row)

    con.commit()
    con.close()

    return result


# [ヘルパ関数] SELECT文で帰ってきたデータの配列を連想配列に変換する
# ※ データベース構造に依存する
def convert_tbl_address(raw_row):
    return({
        'id': raw_row[0],
        'name': raw_row[1],
        'name_yomi': raw_row[2],
        'postal_address': raw_row[3],
        'memo': raw_row[4]
    })


# データ一覧（トップページ）
@app.route('/', methods=['GET'])
def show():
    user_data = []

    for data in execute_sql('SELECT id, name, name_yomi, postal_address, memo FROM tbl_address'):
        user_data.append(convert_tbl_address(data))

    return render_template('index.html', user_data=user_data)
# --- (1) templates/template.html
# ---     templates/index.html を作成し、
# --- address.py をここまで作成して実行し、データの一覧が表形式で表示されることを確認


# [処理] データ挿入
@app.route('/', methods=['POST'])
def insert():
    name = request.form['name']
    name_yomi = request.form['name_yomi']
    address = request.form['postal_address']
    memo = request.form['memo']

    execute_sql(f'INSERT INTO tbl_address (name, name_yomi, postal_address, memo) VALUES ("{name}", "{name_yomi}", "{address}", "{memo}")')

    return show()
# --- (2) address.py をここまで作成して実行し、データの挿入ができることを確認


# 詳細ページ
@app.route('/detail', methods=['POST'])
def detail():
    id = request.form['id']
    # 1行だけしか返らないはずなので、[0]を指定しておく (こんなイメージ: [[1,2,3]] → [1,2,3])
    row_raw = execute_sql(f'SELECT * FROM tbl_address WHERE id = {id}')[0]
    data = convert_tbl_address(row_raw)

    return render_template('detail.html', data=data)
# --- (3) templates/detail.html を作成し、
# address.py をここまで作成して詳細ページが表示できることを確認


# [処理] データ処理
@app.route('/delete', methods=['POST'])
def delete():
    id = request.form['id']
    execute_sql(f'DELETE FROM tbl_address WHERE id = {id}')

    return redirect(url_for('show'))
# --- (4) address.py をここまで作成して実行し、
#         データの削除ができることを確認


# [処理] データ更新
@app.route('/update', methods=['POST'])
def update():
    id = request.form['id']
    name = request.form['name']
    name_yomi = request.form['name_yomi']
    postal_address = request.form['postal_address']
    memo = request.form['memo']

    execute_sql(f'UPDATE tbl_address SET name = "{name}", name_yomi = "{name_yomi}", postal_address = "{postal_address}", memo = "{memo}" WHERE id = {id}')

    return redirect(url_for('show'))
# --- (5) address.py をここまで作成して実行し
#         データの更新ができることを確認
'''.splitlines(keepends=True),
      },
      {
        'type': 'binary',
        'name': 'address.db'
      },
      {
        'type': 'directory',
        'name': 'templates',
        'files': [
          {
            'type': 'file',
            'name': 'index.html',
            'content': '''{% extends 'template.html' %}
{% block main %}
<h1>アドレス一覧</h1>
<table style="border-style: solid">
<tr>
    <th>id</th>
    <th>名前</th>
    <th>名前(よみがな)</th>
    <th>住所</th>
    <th>メモ</th>
    <th></th>
</tr>

{% for data in user_data %}
<tr>
    <td>{{ data['id'] }}</td>
    <td>{{ data['name'] }}</td>
    <td>{{ data['name_yomi'] }}</td>
    <td>{{ data['postal_address'] }}</td>
    <td>{{ data['memo'] }}</td>
    <td>
        <form method="post" action="detail">
            <input type="hidden" name="id" value="{{ data['id'] }}">
            <input type="submit" value="詳細">
        </form>
    </td>
</tr>
{% endfor %}

<tr>
    <td>{{ user_data | length + 1 }}</td>
    <td><input form="insert" name="name" required placeholder="名前"></td>
    <td><input form="insert" name="name_yomi" required placeholder="名前（よみがな) "></td>
    <td><input form="insert" name="postal_address" required placeholder="住所"></td>
    <td><input form="insert" name="memo" required placeholder="メモ"></td>
    <td>
        <form action="/" id="insert" method="post">
            <input type="submit" value="追加">
        </form>
    </td>
</td>
</table>
{% endblock %}
'''.splitlines(keepends=True),
          },
          {
            'type': 'file',
            'name': 'template.html',
            'content': '''<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <title>Address book on SQLite</title>
        <style>
            table, th, td{
                border-collapse: collapse;
                border: solid;
            }
        </style>
    </head>
    <body>
    <header>
        <h1>SQLite3 住所録</h1>
        <h2>---</h2>
    </header>
    <hr />
    {% block main %}
    {% endblock %}
    <hr />
    </main>
    <footer class="td-footer">
        <address>Copyright (c) 2021 ---</address>
    </footer>
    </body>
<html>
'''.splitlines(keepends=True),
          },
          {
            'type': 'file',
            'name': 'detail.html',
            'content': '''{% extends 'template.html' %}
{% block main %}
<h1>プロフィール詳細</h>
<a href="/">
<button style="margin:10px 0">← 一覧に戻る</button>
</a>
<table>
<tr><th>id</td><td>{{data['id']}}</th></tr>
<tr><th>名前</td><td><input name="name" value="{{data['name']}}" form="update_form"></th></tr>
<tr>
    <td>名前 (よみがな) </td><td><input name="name_yomi" value="{{data['name_yomi']}}" form="update_form"></td>
</tr>
<tr>
    <td>住所</td><td><input name="postal_address" value="{{data['postal_address']}}" form="update_form"></td>
</tr>
<tr>
    <td>メモ</td><td><input name="memo" type="textbox" value="{{data['memo']}}" form="update_form"></td>
</tr>
</table>
<form method="post" action="/delete" style="display:inline">
    <input type="hidden" name="id" value="{{ data['id']}}">
    <input type="submit" value="削除" style="background-color: red">
</form>
<form method="post" action="/update" style="display:inline" id="update_form">
    <input type="hidden" name="id" value="{{ data['id']}}">
    <input type="submit" value="更新">
</form>
{% endblock %}
'''.splitlines(keepends=True),
          },
        ],
      },
    ],
  ]

file_tree_errors = []

def diff_file_and_text(filepath, text):
  file = open(filepath, 'r')
  d = difflib.Differ()
  diff = d.compare(text, file.readlines())
  file.close()
  return diff

def file_exist_check(files, basedir = '.'):
  for file in files:
    filepath = basedir + '/' + file['name']

    if file['type'] == 'directory':
      if (not os.path.isdir(filepath)):
        file_tree_errors.append('フォルダ「{}」が存在しません。'.format(filepath))
      file_exist_check(file['files'], filepath)

    elif file['type'] == 'file':
      if (os.path.isfile(filepath)):
        diff = diff_file_and_text(filepath, file['content'])
        output = open(filepath + '.diff', 'w')
        output.writelines('\n'.join(diff))
        output.close()
      else:
        file_tree_errors.append('ファイル「{}」が存在しません。'.format(filepath))
    
    elif file['type'] == 'binary':
      if (not os.path.isfile(filepath)):
        file_tree_errors.append('バイナリファイル「{}」が存在しません。'.format(filepath))

    else: 
      raise SyntaxError('スクリプトに問題があります。')

def main(no):
  if no == None:
    raise ValueError('引数を指定してください。')
  if no not in range(1, len(tree) + 1):
    raise ValueError('問題番号が不正です。')
  
  file_exist_check(tree[no - 1])

if __name__ == '__main__':
  no = input('問題番号を入力してください : ')

  print('\nカレントディレクトリ: {}\n'.format(os.path.dirname(os.path.abspath(__file__))))

  main(int(no))

  if len(file_tree_errors) > 0:
    print('\nファイル構造に問題があります。')
    for error in file_tree_errors:
      print('・' + error)
  else:
    print('\nファイル構造に問題はありません。')
  
  print('\nファイル差分を出力しました。')
  print()