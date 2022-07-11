import twitter
def find_popular_tweets(twitter_api, statuses, retweet_threshold=3):
    # You could also consider using the favorite_count parameter as part of
    # this heuristic, possibly using it to provide an additional boostto
    # popular tweets in a ranked formulation
    return [ status
            for status in statuses
                if status['retweet_count'] > retweet_threshold ]

def twitter_search(twitter_api, q, max_results=200, **kw):
    # See http://bit.ly/2QyGz0P and https://bit.ly/2QyGz0P
    # for details on advanced search criteria that may be useful for
    # keyword arguments
    # See https://dev.twitter.com/docs/api/1.1/get/search/tweets
    search_results = twitter_api.search.tweets(q=q, count=100, **kw)
    statuses = search_results['statuses']
    # Iterate through batches of results by following the cursor until we
    # reach the desired number of results, keeping in mind that OAuth users
    # can "only" make 180 search queries per 15minute interval. See
    # https://developer.twitter.com/en/docs/basics/ratelimits
    # for details. A reasonable number of results is ~1000, although
    # that number of results may not exist for all queries.
    # Enforce a reasonable limit
    max_results = min(1000, max_results)
    
    for _ in range(10): # 10*100 = 1000
        try:
            next_results = search_results['search_metadata']['next_results']
        except KeyError as e: # No more results when next_results doesn't exist
            break
    # Create a dictionary from next_results, which has the following form:
    # ?max_id=313519052523986943&q=NCAA&include_entities=1
        kwargs = dict([ kv.split('=')
            for kv in next_results[1:].split("&") ])
        search_results = twitter_api.search.tweets(**kwargs)
        statuses += search_results['statuses']
    
        if len(statuses) > max_results:
            break
    return statuses

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

#palabra que contendrán la coleccion de tweets extraidos
q = "Crossfit"
twitter_api = oauth_login()
search_results = twitter_search(twitter_api, q, max_results=200)
popular_tweets = find_popular_tweets(twitter_api, search_results)
for tweet in popular_tweets:
    print(tweet['text'], tweet['retweet_count'])
