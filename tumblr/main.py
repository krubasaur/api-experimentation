#!/usr/bin/env python

import requests

import api

def main():
    request = api.Client()
    blog_name = str(input('Blog name:  '))
    posts = request.get_blog(blog_name, 'posts')
    print(posts)




if __name__ == '__main__':
    main()
