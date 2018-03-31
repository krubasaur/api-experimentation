import requests

import credentials

#TODO: make get_tagged_posts() work with new param capabilities (i.e. "limit" is
    # now recognized as a param.) Need to make params format properly for url.

class Client(object):
    host = 'http://api.tumblr.com/'
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
        # print(params)

        try:
            response = requests.get(
                url, params=params
            )

            print('Status Code: {status_code}'.format(
                status_code=response.status_code))
            return response

        except requests.exceptions.RequestException:
            print('HTTP Request failed')

    def get_blog_posts(self, blog, params):
        if params:
            for i in params:
                params = params
        else:
            params = None

        url = self.host + f"v2/blog/{blog}.tumblr.com/posts"
        response = self.get(url, params).json()
        return response

    def get_tagged_posts(self, tag, params):
        if params:
            for i in params:
                params = params
        else:
            params = None
        print(params)
        url = self.host + f"v2/tagged?tag={tag}"
        response = self.get(url, params).json()
        return response
