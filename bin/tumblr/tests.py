#!/usr/bin/env python

import os

from dotenv import find_dotenv, load_dotenv

from lib.tumblr.api import Client

load_dotenv(find_dotenv())

class Tests(object):
    def __init__(self):
        print('class initiated')

    def print_tagged_posts(self, client, tag, limit):
        response = client.get_tagged_posts(tag, limit=limit)
        data = response['response']

        for post in data:
            post = data[data.index(post)]

            blog_name = post['blog_name']
            slug = post['slug']
            post_type = post['type']
            date = post['date']
            timestamp = post['timestamp']
            tags = post['tags']
            short_url = post['short_url']

            print(f"""
            Blog Name: {blog_name}
            Slug: {slug}
            Type: {post_type}
            Date: {date}
            Timestamp: {timestamp}
            Tags: {tags}
            Short URL: {short_url}

            """)

    def print_blog_posts(self, client, blog_id, limit, post_type, tag):
        response = client.get_blog_posts(blog_id, limit=limit, post_type=post_type, tag=tag)
        data = response['response']['posts']

        if limit is not None:
            print(f'Limit: {limit}')
        if post_type is not None:
            print(f'Type: {post_type}')
        if tag is not None:
            print(f'Tag: {tag}')

        for post in data:
            post_type = post['type']
            post_id = post['id']
            post_url = post['post_url']
            slug = post['slug']
            date = post['date']
            timestamp = post['timestamp']
            tags = post['tags']
            short_url = post['short_url']

            print(f"""
            Slug: {slug}
            Type: {post_type}
            Date: {date}
            Timestamp: {timestamp}
            Tags: {tags}
            Short URL: {short_url}

            """)


def main():
    tumblr = Client(os.environ['tumblr_api_key'])

    test1 = Tests()
    test1.print_tagged_posts(tumblr, 'happy', '4')

    test2 = Tests()
    test2.print_blog_posts(tumblr, 'staff', 2, None, None)
    test2.print_blog_posts(tumblr, 'staff', 5, 'text', 'news')
    test2.print_blog_posts(tumblr, 'staff', 1, 'photo', None)



if __name__ == '__main__':
    main()
