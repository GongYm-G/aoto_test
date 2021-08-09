import xlrd, requests
import re, os


class Config:
    def __init__(self):
        self.files_path = os.path.join(os.path.abspath('..'), 'test_files')
        self.config_file = os.path.join(self.files_path, '接口测试运行文件.xls')
        # print(self.name)

    def configFile(self):
        xl = xlrd.open_workbook_xls(self.config_file).sheet_by_index(0)
        value = [xl.row_values(i) for i in range(xl.nrows)]
        for j in value:
            if j[-1] == 'YES':
                # 调用文件处理接口
                file_path = os.path.join(os.path.join(self.files_path, '待运行测试文件'), j[0])
                print(file_path)
                self.a(file_path)
            else:
                pass

    def parameterFormatting(self, path):
        ex = xlrd.open_workbook_xls(path).sheet_by_index(2)
        parameter = [ex.row_values(i) for i in range(1, ex.nrows)]
        for i in range(len(parameter)):
            kyes = [j for j in parameter[i][7:-3:2]]
            values = [k for k in parameter[i][8:-2:2]]
            data = dict(zip(kyes, values))
            try:
                data.pop('')
            except KeyError:
                pass
            yield parameter[i][1:7], data

    def test_run(self, path):
        txt = [i for i in self.parameterFormatting(path)]
        print(txt)
        return txt


if __name__ == '__main__':
    a = []
    c = Config()
    c.configFile()




