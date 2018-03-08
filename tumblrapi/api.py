import params # Private file containing api_key
import requests

url = 'http://api.tumblr.com/v2/blog/krubasaur.tumblr.com/'


# TODO: Consolidate these three now that we know the basic
# functionality works as expected.


def get_blog_info():
    # Get blog info
    try:
        response = requests.get(
            url=url + 'info/',
            params={
                'api_key': params.api_key},
                )
        print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
                content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

def get_blog_posts():
    # Get blog posts
    try:
        response = requests.get(
            url=url + 'posts/',
            params={
                'api_key': params.api_key},
                )
        print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
                content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

def get_avatar():
    # Get blog's avatar
    try:
        response = requests.get(
        url=url + 'avatar/',
        params={
            'api_key': params.api_key},
            )
        print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
                content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

get_blog_info()
get_blog_posts()
get_avatar()
