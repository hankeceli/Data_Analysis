# Databricks notebook source
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  12 10:53:14 2018

@author: hamza.mohammed
"""
from ast import literal_eval
from pyspark import SparkConf, SparkContext
import sys, os, json
os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3'

conf = SparkConf()
sc = SparkContext.getOrCreate()


#2nd version retweetNetwork
def mapTweet(line):
  retweetList = []
    #=========================================================================================
    # Exception handling: when a retweet key  doesn't exist in a particular tweet.
    # ========================================================================================
  try:
    #converting unicode of unique tweets to pure json unique_tweets
    jsonUniqueTweet = json.dumps(line, ensure_ascii=False)
    
    #dict
    response_item = ast.literal_eval(jsonUniqueTweet.encode('utf8'))
    index = json.loads(response_item)
    
    # ===========================================================================================
    #Fetch the user1 and user2 with the number of retweets
    #Making (User1, User2) as Key, while retweet count as the Valeu
    # ===========================================================================================
    user1 = index['user']['id_str']
    user2 = index['retweeted_status']['user']['id_str']
    retweetList.append([user1+ " , "+ user2, 1])
    return retweetList
  except:
    return retweetList




file = sc.textFile('/FileStore/tables/20180624000034')
mapTweets = file.flatMap(lambda line: mapTweet(line))
reducePairUserRetweets = mapTweets.reduceByKey(lambda a,b:a+b).collect()

#print(reducePairUserRetweets)
reducePairUserRetweets.saveAsTextFile('/FileStore/tables/2ndVersRetweetNetwork')


#Checking the content of the save file
#y = sc.textFile('/FileStore/tables/2ndVersRetweetNetwork')
#print(y.collect())
