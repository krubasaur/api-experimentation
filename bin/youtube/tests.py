#!/usr/bin/env python

import os

from dotenv import find_dotenv, load_dotenv

from lib.youtube.api import Client

load_dotenv(find_dotenv())

class Tests(object):
    def __init__(self):
        print('class initiated')

    def print_channel_info(self, client, part, filter):
        params = dict(part=part, **filter)
        response = client.get_channel_info(params)
        data = response['items']


        for post in data:
            post = data[data.index(post)]
            kind = post['kind']

            if part == 'snippet':
                title = ', ' + post['snippet']['title']
            # if part == 'contentDetails':
            #     contentDetails = post['contentDetails']
            else:
                title = ''
                # contentDetails = None

            print(f'{kind}{title}')

    def print_videos_list(self, client, filter):
        params = dict(part='snippet', **filter)
        response = client.get_videos_list(params)
        data = response['items']

        print('Video IDs:')
        for post in data:
            index = data.index(post)
            print(response['items'][index]['id']['videoId'])

def main():
    youtube = Client(os.environ['youtube_api_key'])
    # test1 = Tests()
    # test1.print_channel_info(youtube, 'snippet', {'id': 'UC_x5XG1OV2P6uZZ5FSM9Ttw'})

    # test2 = Tests()
    # test2.print_channel_info(youtube, 'contentDetails', {'forUsername': 'arulvizhy' })
    # test2.print_channel_info(youtube, 'snippet', {'id': 'UCNYrK4tc5i1-eL8TXesH2pg'})
    test3 = Tests()
    test3.print_videos_list(youtube, {'channelId': 'UCroDJPcFCf6DBmHns6Xeb8g', 'maxResults': 15})
if __name__ == '__main__':
    main()
