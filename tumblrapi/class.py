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

    def get(self, url):
        url = self.host + url

        try:
            response = requests.get(
                url, params={'api_key': params.consumer_key}
            )
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
        except requests.exceptions.RequestException:
            print('HTTP Request failed')


def main():
    linebreak = '\n\n' + '=' * 80 + '\n\n'

    print(linebreak + 'BLOG INFO:\n')

    get_blog_info = TumblrRequest()
    get_blog_info.get(url='v2/blog/krubasaur.tumblr.com/info')

    print(linebreak + 'BLOG POSTS:\n')

    get_blog_posts = TumblrRequest()
    get_blog_posts.get(url='v2/blog/krubasaur.tumblr.com/posts')

    print(linebreak + 'BLOG AVATAR:\n')
    get_avatar = TumblrRequest()
    get_avatar.get(url='v2/blog/krubasaur.tumblr.com/avatar')

    print(linebreak + 'TAGGED POSTS:\n')
    get_tagged_posts = TumblrRequest()
    get_tagged_posts.get(url='v2/tagged?tag=happy')

if __name__ == '__main__':
    main()
