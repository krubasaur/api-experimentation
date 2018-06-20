#!/usr/bin/env python

import os, requests

from dotenv import find_dotenv, load_dotenv

from lib.imgur.api import Client

load_dotenv(find_dotenv())

class Tests(object):
    def __init__(self):
        print('class initiated')

    def get_creds(self):
        self.url = input('enter subreddit: ')
        return self.url

def main():
    imgur = Client(os.environ['imgur_client_id'])
    test1 = Tests()
    test1.get_creds()
    imgur.get_subreddit(test1.url)
    imgur.get_post_data(test1.url)

if __name__ == '__main__':
    main()
