import unittest


class GetName:

    def __init__(self):
        self.first = input('first:')
        self.last = input('last:')

    def get_formatted_name(self):
        full_name = self.first + ' ' + self.last
        return full_name.title()


class TestName(unittest.TestCase):

    def setUp(self):
        print(1)

    def tearDown(self):
        print(2)

    # def setUpClass(cls):
    #     print(3)
    #
    # def tearDownClass(cls):
    #     print(4)


    def test_getname(self):
        a=GetName()
        name = a.get_formatted_name()
        self.assertEqual(name, 'A B')


if __name__ == '__main__':
    unittest.main()
