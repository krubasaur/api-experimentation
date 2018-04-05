#!/usr/bin/env python

import os

from dotenv import find_dotenv, load_dotenv

from lib.youtube.api import Client

load_dotenv(find_dotenv())

class Tests(object):
    def __init__(self):
        print('Begin Test')

    def print_videos_list(self, client, channelId=None, forUsername=None, maxResults=None):
        response = client.get_videos_list(channelId, forUsername, maxResults)
        data = response['items']
        if channelId:
            print('Channel ID Search')
        if forUsername:
            print('Username Search')

        print('Video IDs:')
        
        for post in data:
            index = data.index(post)
            videos = response['items'][index]['id']['videoId']
            print(videos)
            return videos

    def find_channel_id(self, client, part=None, forUsername=None):
        if part is None or forUsername is None:
            print('Error: "part" or "forUsername" cannot be None.')
        else:
            response = client.get_channel_info(part, forUsername)
            channelId = response['items'][0]['id']
            return channelId
            print('Channel ID: ' + channelId)


    def find_channel_print_vid_list(self, client, forUsername, maxResults):
        if forUsername is None:
            print('Error: "part" or "forUsername" cannot be None.')
        else:
            part = 'id'
            channelId = self.find_channel_id(client, part, forUsername)
            videos_list = self.print_videos_list(client, channelId, forUsername=None, maxResults=maxResults)

def main():
    youtube = Client(os.environ['youtube_api_key'])

    print_videos_for_user = Tests()
    print_videos_for_user.print_videos_list(youtube, forUsername='arulvizhy')

    print_videos_for_channel = Tests()
    print_videos_for_channel.print_videos_list(youtube, channelId='UCroDJPcFCf6DBmHns6Xeb8g', maxResults=15)

    print_channelId_for_user = Tests()
    print_channelId_for_user.find_channel_id(youtube, part='id', forUsername=None)
    print_channelId_for_user.find_channel_id(youtube, part='id', forUsername='arulvizhy')

    print_vids_for_user = Tests()
    print_vids_for_user.find_channel_print_vid_list(youtube, 'arulvizhy', 5)
if __name__ == '__main__':
    main()
