import csv, re, xlwt


with open(r'C:\Users\Administrator.RY-20190705FBIQ\Desktop\新建文件夹 (2)\jwtestmall.postman_collection.json', 'r', encoding = 'utf-8') as o:
    a = o.readlines()
    aa1 = []
    for i in a:
        if 'name' in i:
            a1=re.split(': ', i)[1]
            aa1.append(a1)
        elif 'method' in i:
            a1=re.split(': ', i)[1]
            aa1.append(a1)
        elif 'key' in i:
            a1=re.split(': ', i)[1]
            if 'Content-Type' in a1:
                pass
            else:
                aa1.append(a1)
        elif 'raw' in i:
            a1 = re.split(': ', i)[1]
            aa1.append(a1)
            aa1.append('\n')
    po = xlwt.Workbook()
    p = po.add_sheet('jk')
    n = 0
    n1 = 0
    for i in range(aa1.count('\n')):
        while True:
            a = aa1[n1]
            if a == '\n':
                n = 0
                n1 += 1
                break
            p.write(i, n, a)
            n += 1
            n1 += 1
    po.save(r'C:\Users\Administrator.RY-20190705FBIQ\Desktop\新建文件夹 (2)\接口.xls')


