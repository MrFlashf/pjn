import re
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

http = urllib3.PoolManager()

years = range(2008,2018)
base_url = 'https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_('

scores = {}

def get_right_table(tables):
  found = False
  i = 0
  while not found:
    i = i + 1
    table = tables[i]
    header_row = table.findAll('tr')[0]
    header_cells = header_row.findAll('th')
    if len(header_cells) > 1:
      if header_cells[1].getText() == 'Drużyna\n':
        found = True
  return tables[i]

def add_to_result(team, points):
  if team in scores:
    scores[team] = scores[team] + points
  else:
    scores[team] = points

def show_scores_table():
  sorted_scores = sorted(scores, key=lambda team: scores[team], reverse=True)
  i = 1
  for team in sorted_scores:
    print(str(i) + '. ' + team + ': ' + str(scores[team]))
    i = i + 1

for i in years:
  page = base_url + str(i) + '/' + str(i+1) + ')'
  print('Przeliczam sezon ' + str(i) + ' / ' + str(i+1) + '...\n')

  response = http.request('GET', page)
  soup = BeautifulSoup(response.data, 'html.parser')

  tables = soup.findAll('table', attrs={'class': 'wikitable'})

  table = get_right_table(tables)

  rows = table.findAll('tr')
  _ = rows.pop(0)
  for row in rows:
    cells = row.findAll('td')
    team = cells[1].getText()
    parsed_team = re.sub(r'\d*(\s\(\w\))*\n', '', team)
    points = cells[9].getText().strip()
    parsed_points = int(re.sub('−', '-', points))
    add_to_result(parsed_team, parsed_points)

show_scores_table()
