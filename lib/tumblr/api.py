import requests

class Client(object):
    host = 'http://api.tumblr.com/'

    def __init__(self, api_key):
        self.api_key = api_key

    def get(self, url, params=None):
        if params is None:
            params = {}
        req_params = dict(api_key=self.api_key, **params)

        try:
            response = requests.get(
                url, params=req_params
            )

            print('Status Code: {status_code}'.format(
                status_code=response.status_code))
            return response

        except requests.exceptions.RequestException:
            print('HTTP Request failed')

    def get_blog_posts(self, blog_name, limit=20):
        url = self.host + f"v2/blog/{blog_name}.tumblr.com/posts"
        params = {'limit': limit}
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
