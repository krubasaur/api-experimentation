#!/usr/bin/env python

import os

from dotenv import find_dotenv, load_dotenv

from lib.tumblr.api import Client

load_dotenv(find_dotenv())

def print_tagged_posts(client, tag, limit):
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
    # posts = response['response']
    # for post in posts:
    #
    #     blog_name = posts['blog_name']
    #     # slug = posts['response'][post_count]['slug']
    #     # post_type = posts['response'][post_count]['type']
    #     # date = posts['response'][post_count]['date']
    #     print(f"""
    #         Tagged Post Data:
    #
    #         \t* Blog Name: {blog_name}
    #         """
    #         )
    #         #
    #         # \t* Post Title: {slug}
    #         # \t* Post Type: {post_type}
    #         # \t* Date Posted: {date}.
    #     post_count =+ 1

def print_blog_posts(client, blog_id, limit, post_type, tag):
    response = client.get_blog_posts(blog_id, limit=limit, post_type=post_type, tag=tag)
    posts = response['response']['posts']
    print('Testing print_blog_posts():')
    if limit is not None:
        print(f'Limit: {limit}')
    if post_type is not None:
        print(f'Type: {post_type}')
    if tag is not None:
        print(f'Tag: {tag}')

    for post in posts:
        post_type = post['type']
        post_id = post['id']
        post_url = post['post_url']
        slug = post['slug']
        date = post['date']
        timestamp = post['timestamp']
        tags = post['tags']
        short_url = post['short_url']

        print(f"""
    Type: {post_type}
    ID: {post_id}
    URL: {post_url}
    Slug: {slug}
    Date: {date}
    Time: {timestamp}
    Tags: {tags}
    Short URL: {short_url}
        """)


def main():
    tumblr = Client(os.environ['tumblr_api_key'])
    nl = os.linesep
    linebreak = nl * 2 + '=' * 80 + nl * 2

    # print(linebreak + 'TAGGED POSTS TEST:' + nl)


    print_tagged_posts(tumblr, 'happy', '4')
    # print_blog_posts(tumblr, 'staff', 2, None, None)
    # print_blog_posts(tumblr, 'staff', 5, 'text', 'news')
    # print_blog_posts(tumblr, 'staff', 1, 'photo', None)

if __name__ == '__main__':
    main()
