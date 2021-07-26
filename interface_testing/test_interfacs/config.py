import xlrd, requests
import re

class Config:

    def __init__(self):
        self.path = r"C:\Users\Administrator.RY-20190705FBIQ\Desktop\新建文件夹 (2)\接口基本信息.xls"

    def parameterFormatting(self):
        ex = xlrd.open_workbook_xls(self.path)
        ex1 = ex.sheet_by_index(2)
        parameter = [ex1.row_values(i) for i in range(1, ex1.nrows)]
        for i in range(len(parameter)):
            kyes = [j for j in parameter[i][7::2]]
            values = [k for k in parameter[i][8::2]]
            data = dict(zip(kyes, values))
            try:
                data.pop('')
            except KeyError:
                pass
            yield parameter[i][1:7], data


    def a(self):
        data = self.parameterFormatting()
        txt = [i for i in data]
        return txt


if __name__ == '__main__':
    a=[]
    c = Config()
    txt = c.a()
    for i in txt:
        if '是' in i[0]:
            a.append(i)
    a.sort()
    print(a)



