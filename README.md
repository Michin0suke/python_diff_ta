# About

ディレクトリ構造のチェックと、お手本とファイルの中身のチェックを行うPythonスクリプトです。

プログラミングの教室や授業で、お手本のソースコードを写経してもらうような状況で活用できます。


# 使い方

## ビルド

チェックスクリプトを1ファイルにまとめるため、あらかじめPythonファイルのビルドを行います。

`correct_files`の直下に問題の種類名のディレクトリを作り、その中にお手本とするファイル群をコピーします。（その際、このリポジトリに含まれるサンプルは削除して問題ありません。）

`config.py`の`CONTENT_FILE_EXT`に指定した拡張子のつくPythonスクリプトでは、中身のDiffをファイルに生成します。

`gen.py`を実行することで、`dist/output.py`を生成できます。


## 実行

生成した`dist/output.py`を、チェックしたいディレクトリにダウンロードさせます。

Githubのソースコードへのリンクを、リダイレクトさせるなどして短縮するといいでしょう。

* Mac / Linux
```sh
curl -L -o check.py michinosuke.com/ta
```

* Windows
```sh
curl.exe -L -o check.py michinosuke.com/ta
```

それから、`python check.py`で実行し、チェックしたい問題の種類を選択すると、チェックが行われます。