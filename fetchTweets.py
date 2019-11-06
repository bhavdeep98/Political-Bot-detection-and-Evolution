# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 20:27:34 2019

@author: Bhavdeep Singh
"""

import tweepy as tw
import pandas as pd
import botometer
import wordcloud 


consumer_key = "8gTOmnBgiP4cQXVgrxOiCS3yX"
consumer_secret = "MfYfaTRaoQJRisZX5KuTAOxs5xENtGcuM4DuI4CFomI1XhPWOb"

# creating an OAuthHandler instance
# refernece https://tweepy.readthedocs.io/en/latest/auth_tutorial.html
auth = tw.OAuthHandler(consumer_key, consumer_secret)

OAUTH_TOKEN = "2223349652-ObLnAWQvXGhUtueTkcIflppxb27B6895ibTHLi9"
OAUTH_TOKEN_SECRET = "cpdE3vEE2RAY00KdqyzG7tdIZSs6YbQu2tdN5lmoCM2Qp"
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


api = tw.API(auth)

# Define the search term and the date_since date as variables
#search_words = ["#uselections","2020elections"]
                
search_words = ["#uselections", "#2020elections", "#2020Election", "#elections2020", "#election2020", "#democratic", "#republican", "#PresidentialElection2020", "PresidentialElections2020"]

date_since = "2019-7-1"

allTweets= []
for search_word in search_words:
    print(search_word)
    # Collect tweets
    tweets = tw.Cursor(api.search,
                  q=search_word,
                  lang="en",
                  since=date_since).items(100)
    """
        .Cursor() returns an object that you can iterate or loop over to access the
        data collected. Each item in the iterator has various attributes that you 
        can access to get information about each tweet including:
        
        - the text of the tweet
        - who sent the tweet
        - the date the tweet was sent
    """
    allTweets.extend([tweet for tweet in tweets]) 

#print([tweet.text for tweet in allTweets])

users_locs = [[tweet.user.screen_name, tweet.user.location, tweet.text] for tweet in allTweets]
#print(users_locs)

tweet_text = pd.DataFrame(data=users_locs, 
                    columns=['user', "location", "tweet"])
#print(tweet_text.iloc[[0]])


### Checking if the given user is a bot or not using botometer API
### botometer is new form of bot or not.
rapidapi_key = "3a8966dd1emsh774846e09c75b00p1a23acjsn4421f8921611"
twitter_app_auth = {
    'consumer_key': consumer_key,
    'consumer_secret': consumer_secret,
    'access_token': OAUTH_TOKEN,
    'access_token_secret': OAUTH_TOKEN_SECRET,
  }

bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

results = {}
for screen_name, result in bom.check_accounts_in(tweet_text['user']):
    print(result['scores'])
    for key,value in result['scores'].items():
        if key in results.keys():
            results[key].append(value)
        else:
            results[key]=[value]
#     results.append(result['scores'])
#    tempDataFrame.reset_index(drop=True)
#    print(tempDataFrame)
#    tweet_text.reset_index(drop=True)
#    tweet_text.join(tempDataFrame)

#print(results)
tempDataFrame = pd.DataFrame.from_dict(results)
print(tempDataFrame)
tweet_text = pd.concat([tweet_text, tempDataFrame], axis=1)
    
#print(tweet_text)
with open('LiveTweets.csv','w', encoding="utf-8") as file:
    file.write(tweet_text.to_csv(index=False))

