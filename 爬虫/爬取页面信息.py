import requests
from lxml import etree

'https://www.telnote.cn/qqwangming/29/28518.htm'

url1 = 'http://www.51testing.com/html/90/category-catid-90-page-2.html'
url = 'http://www.51testing.com/html/90/category-catid-90.html'
# URL链接初始化
a = requests.get(url1)

# 获取页面编码方式
cord = a.apparent_encoding
# 初始化变量转换编码方式
a.encoding = 'GBK'
#a.encoding = cord
# 转文本格式
content = a.text
# 方法转换成web页面标签
doc = etree.HTML(content)
# 通过xpath定位页面元素并文本显示
doc1 = doc.xpath('/html/body/div[6]/div[1]/div[2]/p')
doc2 = doc.xpath('/html/body/div[6]/div[1]/div[2]/p/text()')[0]

txt = open('文本.txt', 'w')

num=1
while True:
    path = r'/html/body/div[6]/div[1]/div[%d]/p/text()' % num
    try:
        doc2 = doc.xpath(path)[0]
        doc2 = ''.join(doc2.split())
    except IndexError as i:
        print(i)
        break
    num += 1
    txt.write(doc2+'\n')
    print(doc2, end='\n')

txt.close()

