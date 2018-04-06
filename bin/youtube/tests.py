#!/usr/bin/env python

import os

from dotenv import find_dotenv, load_dotenv

from lib.youtube.api import Client

load_dotenv(find_dotenv())

class Tests(object):
    def __init__(self):
        print('Begin Test')

    def fetch_videos_list(self, client, channelId, maxResults=None):
        response = client.get_videos_list(channelId, maxResults=maxResults)
        data = response['items']
        for item in data:
            index = data.index(item)
            videos = data[index]['id']['videoId']
            print(videos)

    def find_channel_id(self, client, forUsername=None):
        if forUsername is None:
            print('Error: "forUsername" cannot be None.')
        else:
            response = client.get_channel_id(forUsername)
            channelId = response['items'][0]['id']
            return channelId
            print('Channel ID: ' + channelId)

    def find_channel_fetch_vid_list(self, client, forUsername, maxResults):
        if forUsername is None:
            print('Error: "part" or "forUsername" cannot be None.')
        else:
            channelId = self.find_channel_id(client, forUsername)
            videos = self.fetch_videos_list(client, channelId, maxResults)


def main():
    youtube = Client(os.environ['youtube_api_key'])

    fetch_videos_for_channel = Tests()
    fetch_videos_for_channel.fetch_videos_list(youtube, 'UCroDJPcFCf6DBmHns6Xeb8g', maxResults=15)

    find_channelId_for_user = Tests()
    channelId = find_channelId_for_user.find_channel_id(youtube, forUsername=None)
    channelId = find_channelId_for_user.find_channel_id(youtube, forUsername='arulvizhy')
    print('Channel ID: ' + channelId)

    print_vids_for_user = Tests()
    print_vids_for_user.find_channel_fetch_vid_list(youtube, 'arulvizhy', 15)
if __name__ == '__main__':
    main()
