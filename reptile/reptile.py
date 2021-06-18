import requests
from lxml import etree

url = requests.get('https://www.motk.com')
urltext = url.headers

txt = open('text.txt', 'w')
for a in urltext.keys():
    txt.write(a + ':' + urltext[a] + '\n')
txt.close()
