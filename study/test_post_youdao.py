import unittest
from unittest import mock

from post_youdao import *

class PostYoudaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)


    def test_get_ts(self):
    #    import time
     #   t=time.time()
    #    ts=str(int(round(t * 1000)))
      #  print(ts)
        get_ts=mock.Mock(return_value='1588744853408')
        self.assertEqual('1588744853408',get_ts())


if __name__ == '__main__':
    unittest.main()
