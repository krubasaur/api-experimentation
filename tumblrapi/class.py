import requests

import params

# TODO: * test retrieving other types of data than status_code & content

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
        try:
            response = requests.get(
                url, params={'api_key': params.consumer_key}
            )

            print('Status Code: {status_code}'.format(
                status_code=response.status_code))
            return response

        except requests.exceptions.RequestException:
            print('HTTP Request failed')

    def get_blog_info(self):
        url = self.host + 'v2/blog/krubasaur.tumblr.com/info'
        self.get(url)

    def get_blog_posts(self):
        url = self.host + 'v2/blog/krubasaur.tumblr.com/posts'
        self.get(url)

    def get_avatar(self):
        url = self.host + 'v2/blog/krubasaur.tumblr.com/avatar'
        self.get(url)

    def get_tagged_posts(self):
        url = self.host + 'v2/tagged?tag=happy&limit=1'
        response = self.get(url).json()
        return response
        # print(response['response']) # to see json object options




def main():
    linebreak = '\n\n' + '=' * 80 + '\n\n'


    # print(linebreak + 'BLOG INFO TEST:\n')
    #
    # request = TumblrRequest()
    # request.get_blog_info()
    #
    #
    # print(linebreak + 'BLOG POSTS TEST:\n')
    #
    # request = TumblrRequest()
    # request.get_blog_posts()
    #
    # print(linebreak + 'BLOG AVATAR TEST:\n')
    # request = TumblrRequest()
    # request.get_avatar()
    #

    print(linebreak + 'TAGGED POSTS TEST:\n')
    request = TumblrRequest()
    tagged_posts = request.get_tagged_posts()

    print(tagged_posts) # prints entire response contnets

    print("""
        Tagged Post Data:

        \t* Blog Name: {blog_name}
        \t* Post Type: {type}
        \t* Date Posted: {date}.""".format(
            blog_name=tagged_posts['response'][0]['blog_name'],
            type=tagged_posts['response'][0]['type'],
            date=tagged_posts['response'][0]['date'],
            ))

if __name__ == '__main__':
    main()
