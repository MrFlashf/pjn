import urllib3
import re
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()

for i in [0, 1,2,3,4,5]:
  it = ';0020-30-0-0-' + str(i) + '.htm' if i > 0 else ''

  response = http.request('GET', "https://www.ceneo.pl/Szlifierki_i_polerki/Rodzaj:Szlifierki_katowe.htm"+it)

  soup = BeautifulSoup(response.data, "html.parser")

  links = soup.find_all('a', {'class': 'go-to-product js_conv js_clickHash'})
  for link in links:
    print(link.get_text())

  if i < 5:
    print('Ładuje następne...')
