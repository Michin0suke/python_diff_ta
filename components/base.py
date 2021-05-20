import os, difflib, json

tree = """{{ tree }}"""

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