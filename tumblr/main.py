#!/usr/bin/env python

import requests

import api

def main():
    request = api.Client()
    blog_name = str(input('Blog name:  '))
    posts = request.get_blog(blog_name, 'posts')
    # print(posts)

    # post_count = 5
    #
    # for i in posts:
    print(posts['response']['posts'][0]['id'])
    print(posts['response']['posts'][1]['id'])
    print(posts['response']['posts'][2]['id'])
    print(posts['response']['posts'][3]['id'])

    #     title = posts['response'][post_count]['slug']
    #     post_type = posts['response'][post_count]['type']
    #     date = posts['response'][post_count]['date']
    #     timestamp = posts['response'][post_count]['timestamp']
    #     tags = posts['response'][post_count]['tags']
    #     url = posts['response'][post_count]['short_url']
    #
    #     print(f"""
    #     Posts for @{blog_name}:
    #
    #     * Post ID: {uid}
    #     * Title: {slug}
    #     * Type: {post_type}
    #     * Date: {date}
    #     * Time: {timestamp}
    #     * Tags: {tags}
    #     * Url: {url}
    #     """)
        # post_count =+ 1



if __name__ == '__main__':
    main()
