import requests

import params


class TumblrRequest(object):
    def __init__(
        self,
        consumer_key=params.consumer_key,
        consumer_secret=params.consumer_secret,
        oauth_token=params.oauth_token,
        oauth_secret=params.token_secret,  # change in params.py
        host="http://api.tumblr.com/"
    ):
        self.host = host
        # self.consumer_key = params.consumer_key
        # self.consumer_secret = params.consumer_secret
        # self.oauth_token = params.oauth_token
        # self.oauth_secret = params.oauth_secret
        # self.host = host

    def get(self, url):
        url = self.host + url

        try:
            response = requests.get(
            url, params={params.consumer_key}
            )
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
        except requests.exceptions.RequestException:
            print('HTTP Request failed')


tumblr_request = TumblrRequest()

request = tumblr_request.get(url='v2/blog/krubasaur.tumblr.com/info')
request()
