#!/usr/bin/env python

import os

from dotenv import find_dotenv, load_dotenv

from lib.tumblr.client import Client

load_dotenv(find_dotenv())


def print_blog_posts(client, blog_id, limit):
    response = client.get_blog_posts(blog_id, limit=limit)
    posts = response['response']['posts']
    for post in posts:
        blog_name = post['blog_name']
        slug = post['slug']
        post_type = post['type']
        date = post['date']

        print(
            f"""
            Tagged Post Data:

            \t* Blog Name: {blog_name}
            \t* Post Title: {slug}
            \t* Post Type: {post_type}
            \t* Date Posted: {date}"""
        )


def main():
    tumblr = Client(os.environ['tumblr_api_key'])
    print_blog_posts(tumblr, 'thebroadabroad', 2)


if __name__ == '__main__':
    main()
