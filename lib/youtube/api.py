import requests

class Client(object):
    host = 'https://www.googleapis.com/youtube/v3/'

    def __init__(self, key):
        self.key = key

    def get_channel_info(self, params=None):
        req_url = self.host + 'channels'
        if params is None:
            params = {}
        req_params = dict(key=self.key, part='snippet', id='UC_x5XG1OV2P6uZZ5FSM9Ttw', **params)

        response = requests.get(req_url, params=req_params).json()
        print(response['items'])
