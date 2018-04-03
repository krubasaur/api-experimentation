import requests

class Client(object):
    host = 'https://www.googleapis.com/youtube/v3/'

    def __init__(self, key):
        self.key = key

    def get(self, url, params=None):
        req_url = self.host + url
        if params is None:
            params = {}
        req_params = dict(key=self.key, **params)
        response = requests.get(url, params=req_params)
        return response.json()


    def get_channel_info(self, params):
        url = self.host + 'channels'
        response = self.get(url, params=params)
        return response
