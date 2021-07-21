import pytest


class Test_ABC:

    def setup(self):
        print(1)

    def teardown(self):
        print(2)

    def testa(self):
      print("------->test_a")
      assert 1

    def testb(self):
      print("------->test_b")
      assert 1 != 2


def testb():
    print("------->test_b")
    assert 1 == 2
