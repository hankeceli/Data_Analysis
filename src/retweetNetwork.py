# Databricks notebook source
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 10:53:14 2018

@author: hamza.mohammed
"""

from ast import literal_eval
from pyspark import SparkConf, SparkContext
import sys, os, json, datetime
from operator import add
from pyspark.sql import SparkSession
os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3'

conf = SparkConf()
sc = SparkContext.getOrCreate()


def mapFunc(line):
  tweetJSON = json.loads(line)
  tweet = tweetJSON['id']
  return tweet
  

def redFunc(line1, line2):
	return line2

input = sc.textFile('/FileStore/tables/20180624000034.txt')

output = input.map(lambda x: (mapFunc(x),x)).reduceByKey(lambda x,y: redFunc(x,y)).sortByKey(ascending=False).take(1)


print("The unique tweet-terms are: \n")
#printing pairs (unique_tweet and its ID)
for(id, unique_tweet) in output:
    print("%s: %d" % (unique_tweet, id))
    
    print("\n")
    print("\n")
    print(":::::::::::::::user1, user2: retweet_count(output_Result)::::::::::::: \n")
    

    
print("The output of (user1, user2: retweet_count): ")
response_item = literal_eval(json.dumps(unique_tweet, ensure_ascii=False).encode('utf8'))
index = json.loads(response_item)


print("%d, %d, %d " % (index['id'], 
                           index['retweeted_status']['id'],
                           index['retweeted_status']['retweet_count']))
