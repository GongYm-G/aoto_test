import requests
from lxml import etree

url = requests.get('http://abshu.com/index.php')

url1 = url.text

print(url1)
dom = etree.HTML(url.text)

txt = dom.xpath(r'//*[@id="content"]/div[2]/p/text()')[0]
print(txt)
text = open('text.txt', 'w')
text.write('1,2,3,4,5,6')
text.close()
with open('haha.txt', 'w') as fp:
    fp.write(txt)


