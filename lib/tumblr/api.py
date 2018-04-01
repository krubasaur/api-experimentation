import requests

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
        print('Status Code: {status_code}'.format(
                status_code=response.status_code))
        return response.json()

    def get_blog_posts(self, blog_id, limit=20, post_type=None, tag=None):
        url = f"v2/blog/{blog_id}.tumblr.com/posts"
        params = {'limit': limit}
        if tag:
            params['tag'] = tag
        if post_type:
            params['post_type'] = post_type
        response = self.get(url, params)
        return response

    def get_tagged_posts(self, tag, params):
        if params:
            for i in params:
                params = params
        else:
            params = None
        print(params)
        url = f"v2/tagged?tag={tag}"
        response = self.get(url, params)
        return response
