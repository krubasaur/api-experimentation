import requests

# TODO: make get_tagged_posts() work with new param capabilities (i.e. "limit"
# is now recognized as a param.) Need to make params format properly for url.


class Client(object):
    host = 'http://api.tumblr.com/'

    def __init__(self, api_key):
        self.api_key = api_key

    def get(self, url, params=None):
        req_url = self.host + url

        if params is None:
            params = {}
        req_params = dict(api_key=self.api_key, **params)

        response = requests.get(req_url, params=req_params)
        print(f"Status Code: {response.status_code}")
        return response.json()

    def get_blog(self, blog, page):
        url = f"v2/blog/{blog}.tumblr.com/{page}"
        response = self.get(url)
        return response

    def get_blog_posts(self, blog, params=None):
        url = f"v2/blog/{blog}.tumblr.com/posts"
        response = self.get(url, params)
        return response

    def get_tagged_posts(self, tag, params=None):
        url = f"v2/tagged?tag={tag}"
        response = self.get(url, params)
        return response
