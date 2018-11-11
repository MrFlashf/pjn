import urllib3
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
import subprocess

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()

def get_texts(index):
  language = 'EN' if index == 'index_en' else 'PL'
  print('Pobieram text w języku ' + language + '...')
  base_url = 'http://rjawor.home.amu.edu.pl/'
  language_url = base_url + index

  response = http.request('GET', language_url)
  parsed = BeautifulSoup(response.data, 'html.parser')

  list_items = parsed.find('div', attrs={'id': 'menu'}).find('ul').findAll('li')

  lines = []

  for li in list_items:
    link = li.find('a', href=True)['href']
    combined_url = base_url + link
    response = http.request('GET', combined_url)
    parsed = BeautifulSoup(response.data, 'html.parser')
    paragraphs = parsed.find_all('p')
    for paragraph in paragraphs:
      lines.append(paragraph.text)
  
  print('Pobrałem tekst w języku ' + language)
  return lines

def save_to_file(lines, language, file_name):
  print('Zapisuję to pliku tekst w języku ' + language + '...')
  file = open(file_name, 'w', encoding='utf-8')
  parsed_lines = []
  for line in lines:
    parsed_line = line.replace('\n', '').replace('\t', '')
    parsed_lines.append(parsed_line)
  for text in parsed_lines:
    lines = sent_tokenize(text, language)
    for line in lines:
      file.write(line + '\n')
  file.close()
  print('Zapisałem to pliku tekst w języku ' + language)


pl_index = 'index.php'
en_index = 'index_en.php'

pl_texts = get_texts(pl_index)
save_to_file(pl_texts, 'polish', 'pl.txt')

en_texts = get_texts(en_index)
save_to_file(en_texts, 'english', 'en.txt')

print('Uruchamiam hunalign...')
command = 'hunalign-1.1/src/hunalign/hunalign tmp.dict -text en.txt pl.txt > aligned.txt'
process = subprocess.Popen(command, shell=True)
