# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:51:11 2019

@author: Bhavdeep Singh
"""

import csv
import tweepy 
import os
import json



consumer_key = "8gTOmnBgiP4cQXVgrxOiCS3yX"
consumer_secret = "MfYfaTRaoQJRisZX5KuTAOxs5xENtGcuM4DuI4CFomI1XhPWOb"

# creating an OAuthHandler instance
# refernece https://tweepy.readthedocs.io/en/latest/auth_tutorial.html
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

OAUTH_TOKEN = "2223349652-ObLnAWQvXGhUtueTkcIflppxb27B6895ibTHLi9"
OAUTH_TOKEN_SECRET = "cpdE3vEE2RAY00KdqyzG7tdIZSs6YbQu2tdN5lmoCM2Qp"
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


api = tweepy.API(auth)

dataSetPath = r"C:\Users\Bhavdeep Singh\Downloads\Social Media Mining\Project 2\Dataset"
tsvFileList = []

for file in os.listdir(dataSetPath):
    if file.endswith("tsv"):
        tsvFileList.append(file)
print(tsvFileList)

# refer https://medium.com/@adds68/parsing-tsv-file-with-csv-in-python-662d6347b0cd
#languagesUsed = set()
numberLanguages = {}
with open('summary.csv', 'w') as csvfile:
    fieldnames = ['File Name', 'Deleted Tweets', 'Found Tweet']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for file in tsvFileList:
        deletedTweets = 0
        foundTweets = 0
        with open(dataSetPath+"\\"+file) as tsvFile:
            reader = csv.reader(tsvFile,delimiter ='\t')  
            for row in reader:
                tweet = ""
                try:
                    tweet = api.get_status(row[0])
                except:
                    print("No tweet found")
                label = row[1]
                
                if tweet:
                    foundTweets+=1
                    print(tweet._json['created_at'])
                    print(tweet._json['entities'])
                    print(tweet._json['lang'])
    #                languagesUsed.add(tweet._json['lang'])
                    if tweet._json['lang'] in numberLanguages.keys():
                        numberLanguages[tweet._json['lang']]+=1
                    else:
                        numberLanguages[tweet._json['lang']] = 1
                    print(tweet._json['retweet_count'])
                    print(tweet._json['contributors'])
                else:
                    deletedTweets+=1
                #tweetDict = json.loads(tweet._json)
        writer.writerow({'File Name': file, 'Deleted Tweets': deletedTweets, 'Found Tweet': foundTweets})
#    print(deletedTweets)
#    print(foundTweets)