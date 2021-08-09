import os


class a:
    def __init__(self):
        files_path = os.path.join(os.path.abspath('..'), 'test_files')
        self.name = os.listdir(files_path)
        print(os.path.join(files_path,'接口测试运行文件.xls'))

if __name__ == '__main__':
    a()
