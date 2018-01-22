# encoding: utf-8

import requests

class HTTPRequest():
    def get(self, url):
        result = requests.get(url)
        return result
