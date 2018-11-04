#!/usr/local/bin/python3
import operator
import urllib3
import re
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

http = urllib3.PoolManager()

result = {}

def get_resoults ():
    for i in range (2008, 2018):
        quote_page = 'https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(' + str(i) + '/' + str(i+1) + ')'

        print('Zbieram wyniki z lat ' + str(i) + '/' + str(i+1) + '.')

        response = http.request('GET', quote_page)

        soup = BeautifulSoup(response.data, 'html.parser')

        table= soup.findAll('table', attrs={'class': 'wikitable', 'style': 'text-align: center;'})[1]

        for row in table.findAll('tr'):
            cells = row.findAll('td')
            if(len(cells) >= 9):        
                team = (re.sub(r'\d*(\s\(\w\))*', '', cells[1].get_text().strip()))
                point = int((cells[9].get_text().strip()))
                if team in result:
                    act_points = result[team]
                    result[team] = act_points + point
                else:
                    result[team] = point
        print('Zebrano!')            
    print('\nZebrałem wszystkie wyniki!\n')
    return result

result = get_resoults()
sort_result = sorted(result.items(), reverse=True, key=operator.itemgetter(1))

i = 1

for x in sort_result:
    print(i, x[0], '-',  x[1])
    i = i +1 
