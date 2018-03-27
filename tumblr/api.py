import requests

import credentials

class Client(object):
    def __init__(
        self,
        consumer_key=credentials.consumer_key,
        consumer_secret=credentials.consumer_secret,
        oauth_token=credentials.oauth_token,
        oauth_secret=credentials.oauth_secret,
        host="http://api.tumblr.com/"
    ):
        self.host = host

    def get(self, url, params):
        if params:
            for i in params:
                params = params
        try:
            response = requests.get(
                url, params=params
            )

            print('Status Code: {status_code}'.format(
                status_code=response.status_code))
            return response

        except requests.exceptions.RequestException:
            print('HTTP Request failed')

    def get_blog(self, blog, page):
        url = self.host + f"v2/blog/{blog}.tumblr.com/{page}"
        response = self.get(url).json()
        return response

    def get_blog_posts(self, blog):
        url = self.host + f"v2/blog/{blog}.tumblr.com/posts"
        response = self.get(url, params={'api_key': credentials.consumer_key}).json()
        return response

    def get_tagged_posts(self, tag, limit):
        url = self.host + f"v2/tagged?tag={tag}&limit={limit}"
        response = self.get(url).json()
        return response
