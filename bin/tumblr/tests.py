#!/usr/bin/env python

import os

from dotenv import find_dotenv, load_dotenv

from lib.tumblr.api import Client

load_dotenv(find_dotenv())

def print_tagged_posts(tag, limit):
    request = api.Client()
    posts = request.get_tagged_posts(tag, params={'limit': limit})

    post_count = 0

    for i in posts:

        blog_name = posts['response'][post_count]['blog_name']
        slug = posts['response'][post_count]['slug']
        post_type = posts['response'][post_count]['type']
        date = posts['response'][post_count]['date']

        print(f"""
            Tagged Post Data:

            \t* Blog Name: {blog_name}
            \t* Post Title: {slug}
            \t* Post Type: {post_type}
            \t* Date Posted: {date}."""
            )
        post_count =+ 1


def print_blog_posts(client, blog_id, limit):
    response = client.get_blog_posts(blog_id, limit=limit)
    posts = response['response']['posts']
    for post in posts:
        slug = post['slug']
        print(f'{slug}')


def main():
    tumblr = Client(os.environ['tumblr_api_key'])
    nl = os.linesep
    linebreak = nl * 2 + '=' * 80 + nl * 2

    # print(linebreak + 'TAGGED POSTS TEST:' + nl)


    # print_tagged_posts('happy', '2')
    print_blog_posts(tumblr, 'staff', 2)

if __name__ == '__main__':
    main()
