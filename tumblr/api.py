import requests

import params

class Client(object):
    def __init__(
        self,
        consumer_key=params.consumer_key,
        consumer_secret=params.consumer_secret,
        oauth_token=params.oauth_token,
        oauth_secret=params.oauth_secret,
        host="http://api.tumblr.com/"
    ):
        self.host = host

    def get(self, url):
        try:
            response = requests.get(
                url, params={'api_key': params.consumer_key}
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

    def get_tagged_posts(self, tag, limit):
        url = self.host + f"v2/tagged?tag={tag}&limit={limit}"
        response = self.get(url).json()
        return response
