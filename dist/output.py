import os, difflib, json

tree = {
    "input": {
        "input.py": {
            "type": "file",
            "content": "[\"# input.py: \\u30d5\\u30a9\\u30fc\\u30e0\\u5165\\u529b\\u306e\\u51fa\\u529b\\n\", \"from flask import Flask\\n\", \"from flask import render_template\\n\", \"from flask import request\\n\", \"\\n\", \"app = Flask(__name__)\\n\", \"\\n\", \"# \\u30c8\\u30c3\\u30d7\\n\", \"@app.route('/', methods = ['GET', 'POST']) # POST\\u306e\\u307f\\u5165\\u529b\\u306b\\n\", \"def show_input():\\n\", \"    input = '\\u5165\\u529b\\u306a\\u3057'\\n\", \"    if request.method == 'POST':\\n\", \"        input = request.form['form_input'] # <input name=\\\"form_input\\\" ...>\\n\", \"\\n\", \"    return render_template('index.html', mystr = input)\\n\"]"
        },
        "templates": {
            "type": "directory",
            "children": {
                "index.html": {
                    "type": "file",
                    "content": "[\"{# index.html #}\\n\", \"{% extends 'template.html' %}\\n\", \"{% block main_content %}\\n\", \"<form method=\\\"POST\\\">\\n\", \"    <p>\\u5165\\u529b\\u6587\\u5b57\\u5217: <input type=\\\"text\\\" name=\\\"form_input\\\" size=\\\"30\\\" /></p>\\n\", \"    <p>\\n\", \"        <input type=\\\"submit\\\" value=\\\"\\u5165\\u529b\\u78ba\\u5b9a\\\" />\\n\", \"        <input type=\\\"reset\\\" value=\\\"\\u6d88\\u53bb\\\" />\\n\", \"    </p>\\n\", \"</form>\\n\", \"<!-- \\u5165\\u529b\\u304c\\u3042\\u308c\\u3070\\u6587\\u5b57\\u5217\\u3092\\u633f\\u5165-->\\n\", \"<p>\\u5165\\u529b\\u6587\\u5b57\\u5217:  {{mystr}}</p>\\n\", \"{% endblock %}\\n\"]"
                },
                "template.html": {
                    "type": "file",
                    "content": "[\"<!DOCTYPE html>\\n\", \"<html>\\n\", \"    <header>\\n\", \"        <meta charset=\\\"UTF-8\\\" />\\n\", \"        <title> Second Flask Application by ---</title>\\n\", \"    <body>\\n\", \"        <h1>\\u30d5\\u30a9\\u30fc\\u30e0\\u306e\\u5165\\u529b\\u306e\\u51fa\\u529b</h1>\\n\", \"        <h2>---</h2>\\n\", \"        <hr/>\\n\", \"        {% block main_content %}\\n\", \"        {% endblock %}\\n\", \"        <hr />\\n\", \"        <address>Copyright (c) 2021 ---</address>\\n\", \"    </body>\\n\", \"</html>\\n\"]"
                }
            }
        }
    },
    "address": {
        "address.py": {
            "type": "file",
            "content": "[\"# address.py: \\u4f4f\\u6240\\u9332\\u30a2\\u30d7\\u30ea\\n\", \"from flask import Flask, render_template, request, redirect, url_for\\n\", \"import sqlite3 # SQLite3\\u30d1\\u30c3\\u30b1\\u30fc\\u30b8\\n\", \"\\n\", \"DATABASE_NAME = 'address.db'\\n\", \"app = Flask(__name__)\\n\", \"\\n\", \"\\n\", \"# [\\u30d8\\u30eb\\u30d1\\u95a2\\u6570] SQL\\u3092\\u5b9f\\u884c\\u3059\\u308b\\n\", \"def execute_sql(sql):\\n\", \"    con = sqlite3.connect(DATABASE_NAME)\\n\", \"    cur = con.cursor()\\n\", \"    result = []\\n\", \"\\n\", \"    for row in cur.execute(sql):\\n\", \"        result.append(row)\\n\", \"\\n\", \"    con.commit()\\n\", \"    con.close()\\n\", \"\\n\", \"    return result\\n\", \"\\n\", \"\\n\", \"# [\\u30d8\\u30eb\\u30d1\\u95a2\\u6570] SELECT\\u6587\\u3067\\u5e30\\u3063\\u3066\\u304d\\u305f\\u30c7\\u30fc\\u30bf\\u306e\\u914d\\u5217\\u3092\\u9023\\u60f3\\u914d\\u5217\\u306b\\u5909\\u63db\\u3059\\u308b\\n\", \"# \\u203b \\u30c7\\u30fc\\u30bf\\u30d9\\u30fc\\u30b9\\u69cb\\u9020\\u306b\\u4f9d\\u5b58\\u3059\\u308b\\n\", \"def convert_tbl_address(raw_row):\\n\", \"    return({\\n\", \"        'id': raw_row[0],\\n\", \"        'name': raw_row[1],\\n\", \"        'name_yomi': raw_row[2],\\n\", \"        'postal_address': raw_row[3],\\n\", \"        'memo': raw_row[4]\\n\", \"    })\\n\", \"\\n\", \"\\n\", \"# \\u30c7\\u30fc\\u30bf\\u4e00\\u89a7\\uff08\\u30c8\\u30c3\\u30d7\\u30da\\u30fc\\u30b8\\uff09\\n\", \"@app.route('/', methods=['GET'])\\n\", \"def show():\\n\", \"    user_data = []\\n\", \"\\n\", \"    for data in execute_sql('SELECT id, name, name_yomi, postal_address, memo FROM tbl_address'):\\n\", \"        user_data.append(convert_tbl_address(data))\\n\", \"\\n\", \"    return render_template('index.html', user_data=user_data)\\n\", \"# --- (1) templates/template.html\\n\", \"# ---     templates/index.html \\u3092\\u4f5c\\u6210\\u3057\\u3001\\n\", \"# --- address.py \\u3092\\u3053\\u3053\\u307e\\u3067\\u4f5c\\u6210\\u3057\\u3066\\u5b9f\\u884c\\u3057\\u3001\\u30c7\\u30fc\\u30bf\\u306e\\u4e00\\u89a7\\u304c\\u8868\\u5f62\\u5f0f\\u3067\\u8868\\u793a\\u3055\\u308c\\u308b\\u3053\\u3068\\u3092\\u78ba\\u8a8d\\n\", \"\\n\", \"\\n\", \"# [\\u51e6\\u7406] \\u30c7\\u30fc\\u30bf\\u633f\\u5165\\n\", \"@app.route('/', methods=['POST'])\\n\", \"def insert():\\n\", \"    name = request.form['name']\\n\", \"    name_yomi = request.form['name_yomi']\\n\", \"    address = request.form['postal_address']\\n\", \"    memo = request.form['memo']\\n\", \"\\n\", \"    execute_sql(f'INSERT INTO tbl_address (name, name_yomi, postal_address, memo) VALUES (\\\"{name}\\\", \\\"{name_yomi}\\\", \\\"{address}\\\", \\\"{memo}\\\")')\\n\", \"\\n\", \"    return show()\\n\", \"# --- (2) address.py \\u3092\\u3053\\u3053\\u307e\\u3067\\u4f5c\\u6210\\u3057\\u3066\\u5b9f\\u884c\\u3057\\u3001\\u30c7\\u30fc\\u30bf\\u306e\\u633f\\u5165\\u304c\\u3067\\u304d\\u308b\\u3053\\u3068\\u3092\\u78ba\\u8a8d\\n\", \"\\n\", \"\\n\", \"# \\u8a73\\u7d30\\u30da\\u30fc\\u30b8\\n\", \"@app.route('/detail', methods=['POST'])\\n\", \"def detail():\\n\", \"    id = request.form['id']\\n\", \"    # 1\\u884c\\u3060\\u3051\\u3057\\u304b\\u8fd4\\u3089\\u306a\\u3044\\u306f\\u305a\\u306a\\u306e\\u3067\\u3001[0]\\u3092\\u6307\\u5b9a\\u3057\\u3066\\u304a\\u304f (\\u3053\\u3093\\u306a\\u30a4\\u30e1\\u30fc\\u30b8: [[1,2,3]] \\u2192 [1,2,3])\\n\", \"    row_raw = execute_sql(f'SELECT * FROM tbl_address WHERE id = {id}')[0]\\n\", \"    data = convert_tbl_address(row_raw)\\n\", \"\\n\", \"    return render_template('detail.html', data=data)\\n\", \"# --- (3) templates/detail.html \\u3092\\u4f5c\\u6210\\u3057\\u3001\\n\", \"# address.py \\u3092\\u3053\\u3053\\u307e\\u3067\\u4f5c\\u6210\\u3057\\u3066\\u8a73\\u7d30\\u30da\\u30fc\\u30b8\\u304c\\u8868\\u793a\\u3067\\u304d\\u308b\\u3053\\u3068\\u3092\\u78ba\\u8a8d\\n\", \"\\n\", \"\\n\", \"# [\\u51e6\\u7406] \\u30c7\\u30fc\\u30bf\\u51e6\\u7406\\n\", \"@app.route('/delete', methods=['POST'])\\n\", \"def delete():\\n\", \"    id = request.form['id']\\n\", \"    execute_sql(f'DELETE FROM tbl_address WHERE id = {id}')\\n\", \"\\n\", \"    return redirect(url_for('show'))\\n\", \"# --- (4) address.py \\u3092\\u3053\\u3053\\u307e\\u3067\\u4f5c\\u6210\\u3057\\u3066\\u5b9f\\u884c\\u3057\\u3001\\n\", \"#         \\u30c7\\u30fc\\u30bf\\u306e\\u524a\\u9664\\u304c\\u3067\\u304d\\u308b\\u3053\\u3068\\u3092\\u78ba\\u8a8d\\n\", \"\\n\", \"\\n\", \"# [\\u51e6\\u7406] \\u30c7\\u30fc\\u30bf\\u66f4\\u65b0\\n\", \"@app.route('/update', methods=['POST'])\\n\", \"def update():\\n\", \"    id = request.form['id']\\n\", \"    name = request.form['name']\\n\", \"    name_yomi = request.form['name_yomi']\\n\", \"    postal_address = request.form['postal_address']\\n\", \"    memo = request.form['memo']\\n\", \"\\n\", \"    execute_sql(f'UPDATE tbl_address SET name = \\\"{name}\\\", name_yomi = \\\"{name_yomi}\\\", postal_address = \\\"{postal_address}\\\", memo = \\\"{memo}\\\" WHERE id = {id}')\\n\", \"\\n\", \"    return redirect(url_for('show'))\\n\", \"# --- (5) address.py \\u3092\\u3053\\u3053\\u307e\\u3067\\u4f5c\\u6210\\u3057\\u3066\\u5b9f\\u884c\\u3057\\n\", \"#         \\u30c7\\u30fc\\u30bf\\u306e\\u66f4\\u65b0\\u304c\\u3067\\u304d\\u308b\\u3053\\u3068\\u3092\\u78ba\\u8a8d\"]"
        },
        "address.db": {
            "type": "binary"
        },
        "templates": {
            "type": "directory",
            "children": {
                "index.html": {
                    "type": "file",
                    "content": "[\"{% extends 'template.html' %}\\n\", \"{% block main %}\\n\", \"<h1>\\u30a2\\u30c9\\u30ec\\u30b9\\u4e00\\u89a7</h1>\\n\", \"<table style=\\\"border-style: solid\\\">\\n\", \"<tr>\\n\", \"    <th>id</th>\\n\", \"    <th>\\u540d\\u524d</th>\\n\", \"    <th>\\u540d\\u524d(\\u3088\\u307f\\u304c\\u306a)</th>\\n\", \"    <th>\\u4f4f\\u6240</th>\\n\", \"    <th>\\u30e1\\u30e2</th>\\n\", \"    <th></th>\\n\", \"</tr>\\n\", \"\\n\", \"{% for data in user_data %}\\n\", \"<tr>\\n\", \"    <td>{{ data['id'] }}</td>\\n\", \"    <td>{{ data['name'] }}</td>\\n\", \"    <td>{{ data['name_yomi'] }}</td>\\n\", \"    <td>{{ data['postal_address'] }}</td>\\n\", \"    <td>{{ data['memo'] }}</td>\\n\", \"    <td>\\n\", \"        <form method=\\\"post\\\" action=\\\"detail\\\">\\n\", \"            <input type=\\\"hidden\\\" name=\\\"id\\\" value=\\\"{{ data['id'] }}\\\">\\n\", \"            <input type=\\\"submit\\\" value=\\\"\\u8a73\\u7d30\\\">\\n\", \"        </form>\\n\", \"    </td>\\n\", \"</tr>\\n\", \"{% endfor %}\\n\", \"\\n\", \"<tr>\\n\", \"    <td>{{ user_data | length + 1 }}</td>\\n\", \"    <td><input form=\\\"insert\\\" name=\\\"name\\\" required placeholder=\\\"\\u540d\\u524d\\\"></td>\\n\", \"    <td><input form=\\\"insert\\\" name=\\\"name_yomi\\\" required placeholder=\\\"\\u540d\\u524d\\uff08\\u3088\\u307f\\u304c\\u306a) \\\"></td>\\n\", \"    <td><input form=\\\"insert\\\" name=\\\"postal_address\\\" required placeholder=\\\"\\u4f4f\\u6240\\\"></td>\\n\", \"    <td><input form=\\\"insert\\\" name=\\\"memo\\\" required placeholder=\\\"\\u30e1\\u30e2\\\"></td>\\n\", \"    <td>\\n\", \"        <form action=\\\"/\\\" id=\\\"insert\\\" method=\\\"post\\\">\\n\", \"            <input type=\\\"submit\\\" value=\\\"\\u8ffd\\u52a0\\\">\\n\", \"        </form>\\n\", \"    </td>\\n\", \"</td>\\n\", \"</table>\\n\", \"{% endblock %}\\n\"]"
                },
                "template.html": {
                    "type": "file",
                    "content": "[\"<!DOCTYPE html>\\n\", \"<html>\\n\", \"    <head>\\n\", \"        <meta charset=\\\"UTF-8\\\" />\\n\", \"        <title>Address book on SQLite</title>\\n\", \"        <style>\\n\", \"            table, th, td{\\n\", \"                border-collapse: collapse;\\n\", \"                border: solid;\\n\", \"            }\\n\", \"        </style>\\n\", \"    </head>\\n\", \"    <body>\\n\", \"    <header>\\n\", \"        <h1>SQLite3 \\u4f4f\\u6240\\u9332</h1>\\n\", \"        <h2>---</h2>\\n\", \"    </header>\\n\", \"    <hr />\\n\", \"    {% block main %}\\n\", \"    {% endblock %}\\n\", \"    <hr />\\n\", \"    </main>\\n\", \"    <footer class=\\\"td-footer\\\">\\n\", \"        <address>Copyright (c) 2021 ---</address>\\n\", \"    </footer>\\n\", \"    </body>\\n\", \"<html>\\n\"]"
                },
                "detail.html": {
                    "type": "file",
                    "content": "[\"{% extends 'template.html' %}\\n\", \"{% block main %}\\n\", \"<h1>\\u30d7\\u30ed\\u30d5\\u30a3\\u30fc\\u30eb\\u8a73\\u7d30</h>\\n\", \"<a href=\\\"/\\\">\\n\", \"<button style=\\\"margin:10px 0\\\">\\u2190 \\u4e00\\u89a7\\u306b\\u623b\\u308b</button>\\n\", \"</a>\\n\", \"<table>\\n\", \"<tr><th>id</td><td>{{data['id']}}</th></tr>\\n\", \"<tr><th>\\u540d\\u524d</td><td><input name=\\\"name\\\" value=\\\"{{data['name']}}\\\" form=\\\"update_form\\\"></th></tr>\\n\", \"<tr>\\n\", \"    <td>\\u540d\\u524d (\\u3088\\u307f\\u304c\\u306a) </td><td><input name=\\\"name_yomi\\\" value=\\\"{{data['name_yomi']}}\\\" form=\\\"update_form\\\"></td>\\n\", \"</tr>\\n\", \"<tr>\\n\", \"    <td>\\u4f4f\\u6240</td><td><input name=\\\"postal_address\\\" value=\\\"{{data['postal_address']}}\\\" form=\\\"update_form\\\"></td>\\n\", \"</tr>\\n\", \"<tr>\\n\", \"    <td>\\u30e1\\u30e2</td><td><input name=\\\"memo\\\" type=\\\"textbox\\\" value=\\\"{{data['memo']}}\\\" form=\\\"update_form\\\"></td>\\n\", \"</tr>\\n\", \"</table>\\n\", \"<form method=\\\"post\\\" action=\\\"/delete\\\" style=\\\"display:inline\\\">\\n\", \"    <input type=\\\"hidden\\\" name=\\\"id\\\" value=\\\"{{ data['id']}}\\\">\\n\", \"    <input type=\\\"submit\\\" value=\\\"\\u524a\\u9664\\\" style=\\\"background-color: red\\\">\\n\", \"</form>\\n\", \"<form method=\\\"post\\\" action=\\\"/update\\\" style=\\\"display:inline\\\" id=\\\"update_form\\\">\\n\", \"    <input type=\\\"hidden\\\" name=\\\"id\\\" value=\\\"{{ data['id']}}\\\">\\n\", \"    <input type=\\\"submit\\\" value=\\\"\\u66f4\\u65b0\\\">\\n\", \"</form>\\n\", \"{% endblock %}\\n\"]"
                }
            }
        }
    },
    "hello": {
        "templates": {
            "type": "directory",
            "children": {
                "index.html": {
                    "type": "file",
                    "content": "[\"{# index.html #}\\n\", \"{% extends 'template.html' %}\\n\", \"{% block main_content %}\\n\", \"<!-- \\u6587\\u5b57\\u5217\\u3092\\u633f\\u5165 -->\\n\", \"{{mystr}}\\n\", \"{% endblock %}\\n\"]"
                },
                "template.html": {
                    "type": "file",
                    "content": "[\"<!DOCTYPE html>\\n\", \"<html>\\n\", \"    <header>\\n\", \"        <meta charset=\\\"UTF-8\\\" />\\n\", \"        <title>First Flask Application by ---</title>\\n\", \"    <body>\\n\", \"        <h1>\\u6700\\u521d\\u306eFlask\\u30a2\\u30d7\\u30ea\\u30b1\\u30fc\\u30b7\\u30e7\\u30f3</h1>\\n\", \"        <h2>---</h2>\\n\", \"        <hr />\\n\", \"        {% block main_content %}\\n\", \"        {% endblock %}\\n\", \"        <hr />\\n\", \"        <address>Copyright (c) 2021 ---</address>\\n\", \"    </body>\\n\", \"</html>\\n\"]"
                }
            }
        },
        "hellow.py": {
            "type": "file",
            "content": "[\"# hellow.py: \\u6700\\u521d\\u306eFlask\\u30a2\\u30d7\\u30ea\\n\", \"from flask import Flask\\n\", \"from flask import render_template # \\u8ffd\\u52a0\\n\", \"from flask import request # \\u8ffd\\u52a0\\n\", \"\\n\", \"app = Flask(__name__)\\n\", \"\\n\", \"# \\u30c8\\u30c3\\u30d7\\n\", \"@app.route('/')\\n\", \"def hellow_world():\\n\", \"    mojiretsu = '\\u3088\\u3046\\u3053\\u305d\\u3001Flask\\u306e\\u4e16\\u754c\\u3078\\uff01'\\n\", \"    #print(mojiretsu)\\n\", \"    #return mojiretsu\\n\", \"    return render_template('index.html', mystr = mojiretsu) # \\u8ffd\\u52a0\\n\"]"
        }
    }
}

file_tree_errors = []


def diff_file_and_content(filepath, content):
  file = open(filepath, 'r')
  d = difflib.Differ()
  diff = d.compare(json.loads(content), file.readlines())
  file.close()
  return diff


def file_exist_check(files, basedir = '.'):
  for file in files.items():
    filepath = basedir + '/' + file[0]

    if file[1]['type'] == 'directory':
      if (not os.path.isdir(filepath)):
        file_tree_errors.append('フォルダ「{}」が存在しません。'.format(filepath))
      file_exist_check(file[1]['children'], filepath)

    elif file[1]['type'] == 'file':
      if (os.path.isfile(filepath)):
        diff = diff_file_and_content(filepath, file[1]['content'])
        output = open(filepath + '.diff', 'w')
        output.writelines('\n'.join(diff))
        output.close()
      else:
        file_tree_errors.append('ファイル「{}」が存在しません。'.format(filepath))
    
    elif file[1]['type'] == 'binary':
      if (not os.path.isfile(filepath)):
        file_tree_errors.append('バイナリファイル「{}」が存在しません。'.format(filepath))

    else: 
      raise SyntaxError('スクリプトに問題があります。')


def main(check_type):
  if check_type == None:
    raise ValueError('引数を指定してください。')
  if check_type not in tree.keys():
    raise ValueError('選択された問題が存在しません。')
  
  file_exist_check(tree[check_type])


if __name__ == '__main__':
  print()
  print('[選択できる問題一覧]')
  print('・' + '\n・'.join(tree.keys()))
  print()
  check_type = input('チェックしたい問題を入力してください : ')

  print('\n-------------\n')

  print('[カレントディレクトリ]\n{}\n'.format(os.path.dirname(os.path.abspath(__file__))))

  main(check_type)

  if len(file_tree_errors) > 0:
    print('\n[ファイル構造に問題があります。]')
    for error in file_tree_errors:
      print('・' + error)
  else:
    print('\n[ファイル構造に問題はありません。]')
  
  print('\n[ファイル差分を出力しました。]')
  print()