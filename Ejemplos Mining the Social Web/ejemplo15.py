import twitter
import json

def oauth_login():
# Go to http://twitter.com/apps/new to create an app and get values
# for these credentials that you'll need to provide in place of the
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information
# on Twitter's OAuth implementation.
    CONSUMER_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
    CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
    OAUTH_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
    OAUTH_TOKEN_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api 

twitter_api = oauth_login()
print("""User IDs for retweeters of a tweet by @fperez_org\n""")
print(twitter_api.statuses.retweeters.ids(_id=334188056905129984)['ids'])
print(json.dumps(twitter_api.statuses.show(_id=334188056905129984), indent=1))
print()
print("@SocialWeb's retweet of @fperez_org's tweet\n")
print(twitter_api.statuses.retweeters.ids(_id=345723917798866944)['ids'])
print(json.dumps(twitter_api.statuses.show(_id=345723917798866944), indent=1))
print()
print("@jyeee's retweet of @fperez_org's tweet\n")
print(twitter_api.statuses.retweeters.ids(_id=338835939172417537)['ids'])
print(json.dumps(twitter_api.statuses.show(_id=338835939172417537), indent=1))