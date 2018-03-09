import params# Private file containing api_key
import requests

blog_url = 'http://api.tumblr.com/v2/blog/krubasaur.tumblr.com/'
user_url = 'http://api.tumblr.com/v2/user/'

# TODO: Consolidate these three now that we know the basic
# functionality works as expected.


def get_blog_info():
    # Get blog info
    try:
        response = requests.get(
            url=blog_url + 'info/',
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
            url=blog_url + 'posts/',
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
        url=blog_url + 'avatar/',
        params={
            'api_key': params.api_key},
            )
        print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
                content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

def get_user_info():
    # Get a Tumblr user's info
    try:
        response = requests.get(
        url = user_url + 'info',
        headers={
                "Cookie": "tmgioct=5a2d9f099c8f090631183990",
                "Authorization": "OAuth oauth_consumer_key=\"{consumer_key}\", oauth_nonce=\"{oauth_nonce}\", oauth_signature=\"{oauth_signature}\", oauth_signature_method=\"HMAC-SHA1\", oauth_timestamp=\"1520624036\", oauth_token=\"{oauth_token}\", oauth_version=\"1.0\"".format(consumer_key=params.consumer_key, oauth_nonce=params.oauth_nonce, oauth_signature=params.oauth_signature, oauth_token=params.oauth_token),
            },
        )

        print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
                content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

# get_blog_info()
# get_blog_posts()
# get_avatar()
get_user_info()
