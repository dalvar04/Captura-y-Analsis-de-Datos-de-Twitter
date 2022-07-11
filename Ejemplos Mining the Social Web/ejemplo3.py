import json
import twitter
def twitter_trends(twitter_api, woe_id):
    # Prefix ID with the underscore for query string parameterization.
    # Without the underscore, the twitter package appends the ID value
    # to the URL itself as a specialcase keyword argument.

    return twitter_api.trends.place(_id=woe_id)

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
# Sample usage
twitter_api = oauth_login()
# See https://bit.ly/2pdi0tS

# and http://www.woeidlookup.com to look up different Yahoo! Where On Earth IDs

#tendendias mundiales
"""
WORLD_WOE_ID = 1
world_trends = twitter_trends(twitter_api, WORLD_WOE_ID)
print(json.dumps(world_trends, indent=1))
"""

#tendencias en Estados Unidos
"""
US_WOE_ID = 23424977
us_trends = twitter_trends(twitter_api, US_WOE_ID)
print(json.dumps(us_trends, indent=1))
"""

#tendencias en España
ES_WOE_ID = 23424950
es_trends = twitter_trends(twitter_api, ES_WOE_ID)
print(json.dumps(es_trends, indent=1))