import requests

import params

import client


def print_tagged_posts(tag, limit):
    request = client.TumblrRequest()
    posts = request.get_tagged_posts(tag, limit)

    post_count = 0
    while post_count < limit:
        for i in posts:
            print("""
                Tagged Post Data:

                \t* Blog Name: {blog_name}
                \t* Post Title: {slug}
                \t* Post Type: {type}
                \t* Date Posted: {date}.""".format(
                    blog_name=posts['response'][post_count]['blog_name'],
                    slug=posts['response'][post_count]['slug'],
                    type=posts['response'][post_count]['type'],
                    date=posts['response'][post_count]['date'],
                    ))
            post_count += 1


def main():
    linebreak = '\n\n' + '=' * 80 + '\n\n'


    # print(linebreak + 'BLOG INFO TEST:\n')
    #
    # request = TumblrRequest()
    # request.get_blog_info()
    #
    #
    # print(linebreak + 'BLOG POSTS TEST:\n')
    #
    # request = TumblrRequest()
    # request.get_blog_posts()
    #
    # print(linebreak + 'BLOG AVATAR TEST:\n')
    # request = TumblrRequest()
    # request.get_avatar()
    #

    print(linebreak + 'TAGGED POSTS TEST:\n')
    request = client.TumblrRequest()
    tagged_posts = request.get_tagged_posts('smile', 2)

    print(tagged_posts) # prints entire response contnets

    print(print_tagged_posts('happy', 2))


if __name__ == '__main__':
    main()
