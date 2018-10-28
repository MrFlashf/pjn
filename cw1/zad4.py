import re
import sys

file_name = sys.argv[1]

lines = []
all_mails =[]
with open(file_name) as in_file:
  for line in in_file:
    line_str = line.rstrip()
    mails = re.search("[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*", line_str)
    if mails is not None:
      all_mails.append(mails.group())

print(all_mails)
