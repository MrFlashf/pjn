import re
import sys
from functools import reduce

encoding='UTF-8'

file_name = sys.argv[1]

naughty_words_cores = [
  'kurw',
  'pojeb',
  'jeba',
  'jebi',
  'jeby',
  'huj', # niektórzy jeszcze nie wiedzą, ze powinno być ch
  'java',
  'pierdol',
  'pierdal',
  'kutas',
  'pizd',
  'dup'
]

# generate regex from bad words cores
reg = reduce((lambda output, current: f'{output}[^ ]*{current}[^ ]*|'),naughty_words_cores, '')

reg = reg.rstrip('[^ ]*|') 

new_string = ''

with open(file_name) as in_file:
  for line in in_file:
    line_str = line.rstrip()
    line_array = line_str.split(' ')

    bad_words_in_line = re.findall(reg, line_str)

    line_after_censorship = list(map((lambda x: '---' if x in bad_words_in_line else x), line_array))

    line_after_censorship_string = ' '.join(line_after_censorship)

    new_string += line_after_censorship_string

print(new_string)
