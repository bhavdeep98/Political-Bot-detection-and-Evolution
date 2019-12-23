# -*- coding: utf-8 -*- 
"""
Created on Sun Nov  3 20:27:34 2019

@author: Bhavdeep Singh
"""

import tweepy as tw
import pandas as pd
import botometer
import csv

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#These are the hashtags 
search_words = ["#adult","#milf","#video","#nsfw"]

date_since = "2019-08-01"

header = ['created_at','id','text','hashtags','in_reply_to_status_id',
        'in_reply_to_user_id','user_id','user_name','user_location',
        'user_followers_count','user_friends_count','user_statuses_count',
        'user_verified','user_notifications','retweet_count','favorite_count',
        'favorited','retweeted','possibly_sensitive',
        'possibly_sensitive_appealable','lang','english','universal']

with open("BotOrNot.csv","w") as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()

def writeToCSV(tweet,consumer_key,consumer_secret,OAUTH_TOKEN,OAUTH_TOKEN_SECRET):
    tempDict = dict.fromkeys(header)

    #region check if the value exists or not
    if 'created_at' in tweet._json.keys():
        tempDict['created_at'] = tweet._json['created_at']
    else:
        tempDict['created_at'] = None
        
    if 'id' in tweet._json.keys():
        tempDict['id'] = tweet._json['id']
    else:
        tempDict['id'] = None
    
    if 'text' in tweet._json.keys():
        tempDict['text'] = tweet._json['text']
    else:
        tempDict['text'] = None
    
    if 'hashtags' in tweet._json['entities'].keys():
        tempDict['hashtags'] = tweet._json['entities']['hashtags']
        if len(tempDict['hashtags']) == 0:
            tempDict['hashtags'] = None
        else:
            strhashtag = ""
            for hashtag in range(0,len(tempDict['hashtags'])):
                strhashtag+=str(hashtag)
            tempDict['hashtags'] = strhashtag
    else:
        tempDict['hashtags'] = None
    
    if 'in_reply_to_status_id' in tweet._json.keys():
        tempDict['in_reply_to_status_id'] = tweet._json['in_reply_to_status_id']
    else:
        tempDict['in_reply_to_status_id'] = None
    
    if 'in_reply_to_user_id' in tweet._json.keys():
        tempDict['in_reply_to_user_id'] = tweet._json['in_reply_to_user_id']
    else:
        tempDict['in_reply_to_user_id'] = None
    
    if 'id' in tweet._json['user'].keys():
        tempDict['user_id'] = tweet._json['user']['id']
    else:
        tempDict['user_id'] = None
        
    if 'name' in tweet._json['user'].keys():
        tempDict['user_name'] = tweet._json['user']['name']
    else:
        tempDict['user_name'] = None
    
    if 'location' in tweet._json['user'].keys():
        tempDict['user_location'] = tweet._json['user']['location']
    else:
        tempDict['user_location'] = None
    
    if 'followers_count' in tweet._json['user'].keys():
        tempDict['user_followers_count'] = tweet._json['user']['followers_count']
    else:
        tempDict['user_followers_count'] = None
    
    if 'friends_count' in tweet._json['user'].keys():
        tempDict['user_friends_count'] = tweet._json['user']['friends_count']
    else:
        tempDict['user_friends_count'] = None
    
    if 'statuses_count' in tweet._json['user'].keys():
        tempDict['user_statuses_count'] = tweet._json['user']['statuses_count']
    else:
        tempDict['user_statuses_count'] = None
    
    if 'verified' in tweet._json['user'].keys():
        tempDict['user_verified'] = tweet._json['user']['verified']
    else:
        tempDict['user_verified'] = None
    
    if 'notifications' in tweet._json['user'].keys():
        tempDict['user_notifications'] = tweet._json['user']['notifications']
    else:
        tempDict['user_notifications'] = None
    
    if 'retweet_count' in tweet._json.keys():
        tempDict['retweet_count'] = tweet._json['retweet_count']
    else:
        tempDict['retweet_count'] = None
    
    if 'favorite_count' in tweet._json.keys():
        tempDict['favorite_count'] = tweet._json['favorite_count']
    else:
        tempDict['favorite_count'] = None
    
    if 'favorited' in tweet._json.keys():
        tempDict['favorited'] = tweet._json['favorited']
    else:
        tempDict['favorited'] = None
    
    if 'retweeted' in tweet._json.keys():
        tempDict['retweeted'] = tweet._json['retweeted']
    else:
        tempDict['retweeted'] = None
    
    if 'possibly_sensitive' in tweet._json.keys():
        tempDict['possibly_sensitive'] = tweet._json['possibly_sensitive']
    else:
        tempDict['possibly_sensitive'] = None
    
    if 'possibly_sensitive_appealable' in tweet._json.keys():
        tempDict['possibly_sensitive_appealable'] = tweet._json['possibly_sensitive_appealable']
    else:
        tempDict['possibly_sensitive_appealable'] = None
    
    if 'lang' in tweet._json.keys():
        tempDict['lang'] = tweet._json['lang']
    else:
        tempDict['lang'] = None
    
    # print(tempDict)

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
    
    print(tempDict['user_name'])
    for screen_name, result in bom.check_accounts_in(str(tempDict['user_name'])):
        try:
            print(screen_name+str(result))
            for key,value in result['scores'].items():
                if key in tempDict.keys():
                    if tempDict[key] is not None:
                        tempDict[key].append(value)
                    else:
                        tempDict[key]=[value]
                else:
                    tempDict[key]=[value]
        except Exception as e:
            print(e)    
    with open("BotOrNot.csv","a") as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writerow(tempDict)

for search_word in search_words:
    print("fetching tweets for"+search_word)
    #region auth1
    try:
        consumer_key = "8gTOmnBgiP4cQXVgrxOiCS3yX"
        consumer_secret = "MfYfaTRaoQJRisZX5KuTAOxs5xENtGcuM4DuI4CFomI1XhPWOb"

        # creating an OAuthHandler instance
        # refernece https://tweepy.readthedocs.io/en/latest/auth_tutorial.html
        auth = tw.OAuthHandler(consumer_key, consumer_secret)

        OAUTH_TOKEN = "2223349652-ObLnAWQvXGhUtueTkcIflppxb27B6895ibTHLi9"
        OAUTH_TOKEN_SECRET = "cpdE3vEE2RAY00KdqyzG7tdIZSs6YbQu2tdN5lmoCM2Qp"
        auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

        api = tw.API(auth,wait_on_rate_limit=True)
        tweets = tw.Cursor(api.search,
                      q=search_word,
                      lang="en",
                      since=date_since).items(2)
        # I did this to convert the generator to the list
        extracted_tweets = [tweet for tweet in tweets]
        for tweet in extracted_tweets:
            writeToCSV(tweet,consumer_key,consumer_secret,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
    #endregion
    #region auth2 tweeperror
    except tw.RateLimitError:
        #Use the other key here
        consumer_key = "W6y5Lup84KbpW5dR8KIMTVSqt"
        consumer_secret = "6FCmqr2G32rxD8wGbptCAW3S7mhKowF342tEBieenmBzj2z8oE"

        # creating an OAuthHandler instance
        # refernece https://tweepy.readthedocs.io/en/latest/auth_tutorial.html
        auth = tw.OAuthHandler(consumer_key, consumer_secret)

        OAUTH_TOKEN = "885081121179959296-jKKCMyxHmbybJz4FcYXwtxYmcwU7Xo7"
        OAUTH_TOKEN_SECRET = "OJeZppbRU9yS9m7aPfbZ9WFq35SmfpPLyf7CchTJNkrKz"
        auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

        api = tw.API(auth,wait_on_rate_limit=True)
        tweets = tw.Cursor(api.search,
                      q=search_word,
                      lang="en",
                      since=date_since).items(2)
        extracted_tweets = [tweet for tweet in tweets]
        for tweet in extracted_tweets:
            writeToCSV(tweet,consumer_key,consumer_secret,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
    except Exception as e:
        print("Unexpected error:"+ str(e))
    #endregion
