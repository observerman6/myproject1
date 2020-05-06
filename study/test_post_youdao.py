import unittest
from unittest import mock

from post_youdao import *



class PostYoudaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)


    def test_get_ts(self):
        get_ts=mock.Mock(return_value='1588744853408')
        self.assertEqual('1588744853408',get_ts())

    def test_get_salt(self):
        get_salt=mock.Mock(return_value="15887448534084")
        self.assertEqual('15887448534084',get_salt())

    def test_get_sign(self):
        get_sign=mock.Mock(return_value="2d92614b6687aa594237b0b8dd565f5c")
        self.assertEqual('2d92614b6687aa594237b0b8dd565f5c',get_sign())

if __name__ == '__main__':
    unittest.main()
