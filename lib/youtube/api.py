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

    def get_channel_id(self, forUsername):
        url = self.host + 'channels'
        filters = {}
        if forUsername is not None:
            filters['forUsername'] = forUsername
        params = dict(part='id', **filters)
        response = self.get(url, params=params)
        return response

    def get_videos_list(self, channelId=None, forUsername=None, maxResults=None):
        url = self.host + 'search'
        filters = {'type': 'video'}
        if channelId:
            filters['channelId'] = channelId
        if forUsername:
            filters['forUsername'] = forUsername
        elif maxResults:
            filters['maxResults'] = maxResults

        params = dict(part='snippet', **filters)
        response = self.get(url, params=params)
        return response
