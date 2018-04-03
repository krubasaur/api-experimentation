#!/usr/bin/env python

import os

from dotenv import find_dotenv, load_dotenv

from lib.youtube.api import Client

load_dotenv(find_dotenv())

class Tests(object):
    def __init__(self):
        print('class initiated')

    def print_channel_info(self, client):
        client.get_channel_info()

def main():
    youtube = Client(os.environ['youtube_api_key'])
    test1 = Tests()
    test1.print_channel_info(youtube)

if __name__ == '__main__':
    main()
