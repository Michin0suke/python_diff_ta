# address.py: 住所録アプリ
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