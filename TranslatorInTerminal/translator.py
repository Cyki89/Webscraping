''' 
To use this translate in terminal window add two aliases to .bashrc file :
	alias ang-pol='python (path to script location)/translator.py ang-pol'
	alias pol-ang='python (path to script location)/translator.py pol-ang' 
'''

import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup

command = sys.argv

if len(command) > 4:
	raise SystemExit('Cant pass no more that two word')

translator = {
	'ang-pol' : 'angielski-polski',
	'pol-ang' : 'polski-angielski'
}

url = f'https://pl.bab.la/slownik/{translator[command[1]]}/{"-".join(command[2:])}'

with urlopen(url) as response:
    soup = BeautifulSoup(response.read(), 'html.parser') 

section = soup.select("ul.sense-group-results")
translations = section[0].select('li')

output = " ".join([translation.get_text() for translation in translations])
input_word = " ".join(command[2:])

if len(section) == 1:
	raise SystemExit(f'Cant find translation for {input_word}. Check similar words:\n{output}')

print(f'{input_word} --> {output}')