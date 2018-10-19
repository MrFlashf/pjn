import re
import sys

file_name = sys.argv[1]

with open(file_name) as in_file:
  for line in in_file:
    line_str = line.rstrip()
    print(f'{line_str}')
    if re.match('^.+;\d+;\d+$', f'{line_str}') is None:
      print('error')
