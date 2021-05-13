import os
import difflib

tree = [
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
            'content': '''<!DOC'TYPE' html>
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
    ]
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

    else: 
      raise SyntaxError('スクリプトに問題があります。')

def main(no):
  if no == None:
    raise ValueError('引数を指定してください。')
  if no not in [1]:
    raise ValueError('問題番号が不正です。')
  
  file_exist_check(tree[no - 1])

if __name__ == '__main__':
  no = input('問題番号を入力してください : ')
  main(int(no))
  if len(file_tree_errors) > 0:
    print('\nファイル構造に問題があります。')
    for error in file_tree_errors:
      print('・' + error)
  else:
    print('\nファイル構造に問題はありません。')
  
  print('\nファイル差分を出力しました。')
  print()