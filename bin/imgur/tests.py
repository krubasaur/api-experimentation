#!/usr/bin/env python

import os

from dotenv import find_dotenv, load_dotenv

from lib.imgur.api import get_subreddit

load_dotenv(find_dotenv())

class Tests(object):
    def __init__(self):
        print('class initiated')

    def get_creds(self):
        self.url = input('enter URL: ')
        self.clientId = input('enter clientId: ')
        return self.url, self.clientId

def main():
    test = Tests()
    test.get_creds()
    get_subreddit(test.url, test.clientId)

if __name__ == '__main__':
    main()
