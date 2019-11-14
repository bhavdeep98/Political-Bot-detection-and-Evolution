# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:15:06 2019

@author: Bhavdeep Singh
"""
import csv
import tweepy 
import botometer
import pandas as pd
import os


#backup Previous file(just rename it)
# delete BotOrNot if it exists
os.remove("BotORNot.csv")
header = ['created_at','id','text','hashtags','in_reply_to_status_id',
        'in_reply_to_user_id','user_id','user_name','user_location',
        'user_followers_count','user_friends_count','user_statuses_count',
        'user_verified','user_notifications','retweet_count','favorite_count',
        'favorited','retweeted','possibly_sensitive',
        'possibly_sensitive_appealable','lang']


with open('BotORNot.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(header)


dataSetPath = r"C:\Users\Bhavdeep Singh\Downloads\Social Media Mining\Project 2\Dataset"
fileList = ["political-bots-2019.tsv"]
# refer https://medium.com/@adds68/parsing-tsv-file-with-csv-in-python-662d6347b0cd
with open('summary.csv', 'w') as csvfile:
    #this is just the summary in the sense I am trying to find which tweets 
    #are there and which are not anymore avaialble in a given dataset 
    fieldnames = ['File Name', 'Deleted Tweets', 'Found Tweet', 'Users']
    
    # variable for the counts
    deletedTweets = 0
    foundTweets = 0
    foundUsers = 0
    
    #iterate over the files
    for file in fileList:
        # the files We have so far are mostly csv or tsv
        with open(dataSetPath+"\\"+file) as tsvFile:
            if file.endswith("tsv"):
                reader = csv.reader(tsvFile,delimiter ='\t')
            else:
                reader = csv.reader(tsvFile)
                next(reader)
            for row in reader:
                print(row)
                tweet = ""
                user = ""
                try:
                    consumer_key = "8gTOmnBgiP4cQXVgrxOiCS3yX"
                    consumer_secret = "MfYfaTRaoQJRisZX5KuTAOxs5xENtGcuM4DuI4CFomI1XhPWOb"
                    
                    # creating an OAuthHandler instance
                    # refernece https://tweepy.readthedocs.io/en/latest/auth_tutorial.html
                    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                    
                    OAUTH_TOKEN = "2223349652-ObLnAWQvXGhUtueTkcIflppxb27B6895ibTHLi9"
                    OAUTH_TOKEN_SECRET = "cpdE3vEE2RAY00KdqyzG7tdIZSs6YbQu2tdN5lmoCM2Qp"
                    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
                    
                    
                    api = tweepy.API(auth)
                    tweet = api.get_status(row[0])
                #http://docs.tweepy.org/en/v3.5.0/api.html
                except tweepy.RateLimitError:
                    #Use the other key here
                    consumer_key = "W6y5Lup84KbpW5dR8KIMTVSqt"
                    consumer_secret = "6FCmqr2G32rxD8wGbptCAW3S7mhKowF342tEBieenmBzj2z8oE"
                    
                    # creating an OAuthHandler instance
                    # refernece https://tweepy.readthedocs.io/en/latest/auth_tutorial.html
                    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                    
                    OAUTH_TOKEN = "885081121179959296-jKKCMyxHmbybJz4FcYXwtxYmcwU7Xo7"
                    OAUTH_TOKEN_SECRET = "OJeZppbRU9yS9m7aPfbZ9WFq35SmfpPLyf7CchTJNkrKz"
                    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
                    
                    
                    api = tweepy.API(auth)
                    
                    tweet = api.get_status(row[0])
                except tweepy.TweepError:
                    try:
                        #Use the other key here
                        consumer_key = "W6y5Lup84KbpW5dR8KIMTVSqt"
                        consumer_secret = "6FCmqr2G32rxD8wGbptCAW3S7mhKowF342tEBieenmBzj2z8oE"
                        
                        # creating an OAuthHandler instance
                        # refernece https://tweepy.readthedocs.io/en/latest/auth_tutorial.html
                        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                        
                        OAUTH_TOKEN = "885081121179959296-jKKCMyxHmbybJz4FcYXwtxYmcwU7Xo7"
                        OAUTH_TOKEN_SECRET = "OJeZppbRU9yS9m7aPfbZ9WFq35SmfpPLyf7CchTJNkrKz"
                        auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
                        
                        
                        api = tweepy.API(auth,wait_on_rate_limit=True)
                        
                        tweet = api.get_status(row[0])
                    except:
                        print("No tweet found")
#                except:
#                    print("No tweet found")
#                    try:
#                        user = api.get_user(row[0])
#                    except:
#                        print("Even no user found")
                # label = row[1]
                
                if tweet:
                    foundTweets+=1
                    # a typical tweet with the user info 
                    # I haven't handeled missing values might need to do that here
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
                    
                    
                    #endRegion
                    
                    
                    with open('BotORNot.csv','a', encoding="utf-8") as file:
                        #region Setting up botometer
                        
                        rapidapi_key = "3a8966dd1emsh774846e09c75b00p1a23acjsn4421f8921611"
                        
                        consumer_key = "W6y5Lup84KbpW5dR8KIMTVSqt"
                        consumer_secret = "6FCmqr2G32rxD8wGbptCAW3S7mhKowF342tEBieenmBzj2z8oE"
                        OAUTH_TOKEN = "885081121179959296-jKKCMyxHmbybJz4FcYXwtxYmcwU7Xo7"
                        OAUTH_TOKEN_SECRET = "OJeZppbRU9yS9m7aPfbZ9WFq35SmfpPLyf7CchTJNkrKz"
                        
                        twitter_app_auth = {
                            'consumer_key': consumer_key,
                            'consumer_secret': consumer_secret,
                            'access_token': OAUTH_TOKEN,
                            'access_token_secret': OAUTH_TOKEN_SECRET,
                        }
                        
                        bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)
                            
                        #endregion
                        
                        results = {}
                        result  = bom.check_accounts_in(tweet._json['user']['name'])
                        
                        scoresDict = list(result)[0][1]
                        if 'scores' in scoresDict.keys():
                            for key,value in scoresDict['scores'].items():
                                if key in results.keys():
                                    results[key].append(value)
                                else:
                                    results[key]=value
#                        tempDict.update(results)
                        for key,value in results.items():
                            tempDict[key]=value
#                        print(tempDict)
                        tweetDictPandas = pd.DataFrame(data=tempDict , index=[0])
#                        tweetDictPandas.transpose()
                        file.write(tweetDictPandas.to_csv(header=False))
                elif user:
                    print(user)
                    foundUsers+=1
                else:
                    deletedTweets+=1