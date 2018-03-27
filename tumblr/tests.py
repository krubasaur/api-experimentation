import os

import main, api


def print_tagged_posts(tag, limit):
    request = api.Client()
    posts = request.get_tagged_posts(tag, limit)

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


def print_blog_posts():
    request = api.Client()

    blog_name = str(input('Blog name:  '))
    posts = request.get_blog_posts(blog_name)#, params={'limit': '5'})

    print(posts['response']['posts'][0]['id'])
    print(posts['response']['posts'][1]['id'])
    print(posts['response']['posts'][2]['id'])
    print(posts['response']['posts'][3]['id'])

def main():
    # nl = os.linesep
    # linebreak = nl * 2 + '=' * 80 + nl * 2
    #
    # print(linebreak + 'TAGGED POSTS TEST:' + nl)
    # request = api.Client()
    # tagged_posts = request.get_tagged_posts('smile', 2)
    #
    # # print(tagged_posts) # prints entire response contnets

    # print_tagged_posts('happy', 2)
    print_blog_posts()

if __name__ == '__main__':
    main()
