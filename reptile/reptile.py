import requests
from lxml import etree

url = requests.get('http://abshu.com/index.php')

url1 = url.text
print(url1)
dom = etree.HTML(url.text)

txt = dom.xpath(r'//*[@id="content"]/div[2]/p/text()')[0]

text = open('text.txt', 'w')
text.write('1,2,3,4,5,6')
print(txt)