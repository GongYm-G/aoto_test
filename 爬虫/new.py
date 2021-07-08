import requests
from lxml import etree


class PaChOng:

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def initialize(self):
        """初始化页面并返回页面文本"""
        # URL链接初始化
        a = requests.get(self.url).encoding = 'GBK'
        # 初始化变量转换编码方式
        content = a.text
        return content

    def elem(self):
        doc = etree.HTML(self.initialize())
        doc1 = doc.xpath(self.path)[0]
        return doc1

    def text(self):
        txt = open('文本.txt', 'w')
        txt.write(self.elem() + '\n')