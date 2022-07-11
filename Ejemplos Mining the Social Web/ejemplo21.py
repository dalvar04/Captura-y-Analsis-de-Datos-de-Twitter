import json
from flask import Flask, request
import multiprocessing
from threading import Timer
from IPython.display import IFrame
from IPython.display import display
from IPython.display import Javascript as JS
import twitter
from sys import maxsize as maxint
from functools import partial
import sys

def make_twitter_request(twitter_api_func, max_errors=10, *args, **kw):
# A nested helper function that handles common HTTPErrors. Returns an updated
# value for wait_period if the problem is a 500-level error. Blocks until the
# rate limit is reset if it's a ratelimitingissue (429 error). Returns None
# for 401 and 404 errors, which require special handling by the caller.
    def handle_twitter_http_error(e, wait_period=2, sleep_when_rate_limited=True):

        if wait_period > 3600: # Seconds
            print('Too many retries. Quitting.', file=sys.stderr)
            raise e
            # See https://developer.twitter.com/en/docs/basics/responsecodes
            # for common codes
        if e.e.code == 401:
            print('Encountered 401 Error (Not Authorized)', file=sys.stderr)
            return None
        elif e.e.code == 404:
            print('Encountered 404 Error (Not Found)', file=sys.stderr)
            return None
        elif e.e.code == 429:
            print('Encountered 429 Error (Rate Limit Exceeded)', file=sys.stderr)
            if sleep_when_rate_limited:
                print("Retrying in 15 minutes...ZzZ...", file=sys.stderr)
                sys.stderr.flush()
                time.sleep(60*15 + 5)
                print('...ZzZ...Awake now and trying again.', file=sys.stderr)
                return 2
            else:
                raise e # Caller must handle the ratelimiting issue
        elif e.e.code in (500, 502, 503, 504):
            print('Encountered {0} Error. Retrying in {1} seconds'\
                  .format(e.e.code, wait_period), file=sys.stderr)
            time.sleep(wait_period)
            wait_period *= 1.5
            return wait_period
        else:
            raise e
    
    # End of nested helper function
    
    wait_period = 2
    error_count = 0
            
    while True:
        try:
            return twitter_api_func(*args, **kw)
        except twitter.api.TwitterHTTPError as e:
            error_count = 0
            wait_period = handle_twitter_http_error(e, wait_period)
            if wait_period is None:
                return
        except URLError as e:
            error_count += 1
            time.sleep(wait_period)
            wait_period *= 1.5
            print("URLError encountered. Continuing.", file=sys.stderr)
            if error_count > max_errors:
                print("Too many consecutive errors...bailing out.", file=sys.stderr)
                raise
        except BadStatusLine as e:
            error_count += 1
            time.sleep(wait_period)
            wait_period *= 1.5
            print("BadStatusLine encountered. Continuing.", file=sys.stderr)
            if error_count > max_errors:
                print("Too many consecutive errors...bailing out.", file=sys.stderr)
                raise

def setwise_friends_followers_analysis(screen_name, friends_ids, followers_ids):

    friends_ids, followers_ids = set(friends_ids), set(followers_ids)
    print('{0} is following {1}'.format(screen_name, len(friends_ids)))
    print('{0} is being followed by {1}'.format(screen_name, len(followers_ids)))
    print('{0} of {1} are not following {2} back'.format(
    len(friends_ids.difference(followers_ids)),
    len(friends_ids), screen_name))
    print('{0} of {1} are not being followed back by {2}'.format(
    len(followers_ids.difference(friends_ids)),
    len(followers_ids), screen_name))
    print('{0} has {1} mutual friends'.format(
    screen_name, len(friends_ids.intersection(followers_ids))))

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

def get_friends_followers_ids(twitter_api, screen_name=None, user_id=None,friends_limit=maxint, followers_limit=maxint):

    # Must have either screen_name or user_id (logical xor)
    assert (screen_name != None) != (user_id != None),"Must have screen_name or user_id, but not both"
    # See http://bit.ly/2GcjKJP and http://bit.ly/2rFz90N for details
    # on API parameters
    get_friends_ids = partial(make_twitter_request, twitter_api.friends.ids,count=5000)
    get_followers_ids = partial(make_twitter_request, twitter_api.followers.ids,count=5000)
    friends_ids, followers_ids = [], []
    for twitter_api_func, limit, ids, label in [[get_friends_ids, friends_limit, friends_ids, "friends"],[get_followers_ids, followers_limit, followers_ids, "followers"]]:
        if limit == 0: continue
        cursor = -1
        while cursor != 0:
            # Use make_twitter_request via the partially bound callable
            if screen_name:
                response = twitter_api_func(screen_name=screen_name, cursor=cursor)
            else: # user_id
                response = twitter_api_func(user_id=user_id, cursor=cursor)
            if response is not None:
                ids += response['ids']
                cursor = response['next_cursor']
                print('Fetched {0} total {1} ids for {2}'.format(len(ids),label, (user_id or screen_name)),file=sys.stderr)
                # You may want to store data during each iteration to provide an
                # additional layer of protection from exceptional circumstances
                if len(ids) >= limit or response is None:
                    break
                # Do something useful with the IDs, like store them to disk
    return friends_ids[:friends_limit], followers_ids[:followers_limit]

    
#Sample usage

#usuario del que obtener seguidores y usuarios seguidos
screen_name = "unileon"
twitter_api = oauth_login()
friends_ids, followers_ids = get_friends_followers_ids(twitter_api,screen_name=screen_name)
setwise_friends_followers_analysis(screen_name, friends_ids, followers_ids)
