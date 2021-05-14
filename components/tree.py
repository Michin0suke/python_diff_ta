import os, glob, json

correct_files = {}

def gen_obj(type, path, filename):
  if type == 'file':
    content = open(path, 'r').readlines()
    return {
      'type': 'file',
      'content': json.dumps(content),
    }
  
  elif type == 'directory':
    return {
      'type': 'directory',
      'children': {}
    }

  elif type == 'binary':
    return {
      'type': 'binary',
    }

  else:
    raise SystemError()


def push_tree(path, type):
  path_arr = path.split('/')
  path_arr.pop(0)
  root_key = path_arr.pop(0)
  
  if root_key not in correct_files.keys():
    correct_files[root_key] = {}
  parent = correct_files[root_key]

  while(len(path_arr) > 1):
    parent = parent[path_arr.pop(0)]['children']
  
  if len(path_arr) == 0:
    parent = gen_obj(type, path, root_key)
  else:
    filename = path_arr[0]
    parent[filename] = gen_obj(type, path, filename)

  

def main(config):
  files = glob.glob('correct_files/**/*', recursive=True)

  for path in files:
    type = ''
    if os.path.isdir(path):
      type = 'directory'
    elif os.path.splitext(os.path.basename(path))[1] in config.CONTENT_FILE_EXT:
      type = 'file'
    else:
      type = 'binary'
    
    push_tree(path, type)
  
  return correct_files

if __name__ == '__main__':
  main()