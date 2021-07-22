import csv, re


with open(r'C:\Users\Administrator.RY-20190705FBIQ\Desktop\新建文件夹 (2)\jwtestmall.postman_collection.json', 'r', encoding = 'utf-8') as o:
    a = o.readlines()
    aa1=[]
    for i in a:
        with open(r'C:\Users\Administrator.RY-20190705FBIQ\Desktop\新建文件夹 (2)\接口.csv', 'a') as po:
            po1 = csv.writer(po)
            if 'name' in i:
                a1=re.split(': ', i)[1]
                aa1.append(a1)
            elif 'method' in i:
                a1=re.split(': ', i)[1]
                aa1.append(a1)
            elif 'key' in i:
                a1=re.split(': ', i)[1]
                if 'Content-Type' in a1[1]:
                    pass
                else:
                    aa1.append(a1)
            elif 'raw' in i:
                a1=re.split(': ', i)[1]
                aa1.append(a1)
            print(aa1)
            po1.writerow(aa1)

