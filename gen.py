import json
from components import tree
import config

def main():
  base_file = open('./components/base.py', 'r')
  output_file = open('./dist/output.py', 'w')
  base = ''.join(base_file.readlines())
  tree_str = json.dumps(tree.main(config), indent=4)
  output_str = base.replace('"""{{ tree }}"""', tree_str)
  output_file.write(output_str)

if __name__ == '__main__':
  main()