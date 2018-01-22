# encoding: utf-8
import unittest
import requests
from parameterized import parameterized


class Test_ping(unittest.TestCase):
    def setUp(self):
        print 'setUp'

    @parameterized.expand([
        ('sohu', 'http://www.sohu.com', 200),
        ('163', 'http://www.163.com', 302)
    ])
    def test_ping(self, info, url, result):
        r = requests.get(url)
        self.assertEqual(r.status_code, result)


    def tearDown(self):
        print 'tear down'
