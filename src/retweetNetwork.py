# Databricks notebook source
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  12 10:53:14 2018
@author: hamza.mohammed
"""
from ast import literal_eval
from pyspark import SparkConf, SparkContext
import sys, json


conf = SparkConf()
sc = SparkContext.getOrCreate()


#2nd version retweetNetwork
def mapTweet(line):
  retweetList = []
    #============================================================================================
    # Exception handling: when a retweet key  doesn't exist in a particular tweet.
    # ===========================================================================================
    
  #converting unicode of unique tweets to pure json unique_tweets
  jsonUniqueTweet = json.dumps(line, ensure_ascii=False)
  
  #dict
  response_item = literal_eval(jsonUniqueTweet.encode('utf8'))
  
  
  try:
    index = json.loads(response_item)
    # ===========================================================================================
    #Fetch the user1 and user2 with the number of retweets
    #Making (User1, User2) as Key, while retweetCount as the Value
    # ===========================================================================================
    retweetList.append([index.get('user').get('id_str')+ " , "+ index.get('retweeted_status').get('user').get('id_str'), 1])
    return retweetList
  except:
     return retweetList
  return retweetList



#Large File (20180624234201)
file = sc.textFile('/FileStore/tables/20180624000034')
mapTweets = file.flatMap(lambda line: mapTweet(line))
reducePairUserRetweets = mapTweets.reduceByKey(lambda a,b:a+b).collect()

print(reducePairUserRetweets)
#Saving to directory
#reducePairUserRetweets.saveAsTextFile('/FileStore/tables/2ndVersRetweetNetwork')


#Checking the content of the save file
#y = sc.textFile('/FileStore/tables/2ndVersRetweetNetwork')
#print(y.collect())
