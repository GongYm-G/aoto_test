import xlrd,xlwt,requests
from xlutils.copy import copy



class Config:

    def __init__(self):
        self.path = 'C:\\Users\\Administrator.RY-20190705FBIQ\\Desktop\\新建文件夹 (2)\\接口基本信息.xls'


    def test_interface(self,url,data,jg):
        # url = 'http://10.0.3.75:8080/jwshoplogin/user/login.do'
        # data={
        #     'username':'qwerty',
        #     'password':'123456'
        # }
        r = requests.post(url, data)
        print(r.text,jg)
        print(r.text.find(jg))
        if r.text.find(jg) != -1:
            return '测试通过'
        else:
            return '测试失败', r.text

    def open(self):
        ex = xlrd.open_workbook_xls(self.path)
        ex1 = ex.sheet_by_index(2)
        sheet = ex.sheet_names()[2]
        cop = copy(ex)
        cop1=cop.get_sheet(sheet)
        values = [ex1.row_values(i) for i in range(1, ex1.nrows)]
        for i in range(len(values)):
            a = [i for i in values[i][3:14:2]]
            b = [i for i in values[i][4:15:2]]
            di = dict(zip(a, b))
            try:
                di.pop('')
            except KeyError:
                pass
            a = self.test_interface(values[i][2], di,values[i][-3])
            if '测试通过' == a:
                cop1.write(i+1, 16, a)
            else:
                cop1.write(i+1, 16, a[0])
                cop1.write(i+1, 17, a[1])
        cop.save('C:\\Users\\Administrator.RY-20190705FBIQ\\Desktop\\新建文件夹 (2)\\接口基本信息2.xls')








if __name__ == '__main__':
    c=Config()
    c.open()