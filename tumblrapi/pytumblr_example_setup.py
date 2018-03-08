import pytumblr

# add your app's personal key and oath token credentials into the fields below

client = pytumblr.TumblrRestClient(
    '<consumer_key>',
    '<consumer_secret>',
    '<oath_token>',
    '<oath_secret>'
)

client.info() # Grabs the current user info
