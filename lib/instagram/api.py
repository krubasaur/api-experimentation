import requests

class Client(object):
    host = 'https://api.instagram.com/v1/'

    def __init__(self, access_token):
        self.access_token = access_token
