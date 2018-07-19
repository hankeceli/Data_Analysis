#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys, json
import pandas as pd
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3.3'

conf = SparkConf()
sc = SparkContext(conf = conf)

keywords={} # group : keys (Dict)
groups = [] # groups
tweets = [] # text, year, month, day

filepath = 'keywords-groups.txt'

ch = [('ç','c'),('Ç','C'),('ı','i'),('İ','I'),('ğ','g'),('Ğ','G'),('ü','u'),('ö','o'),('Ş','S'),('ş','s'),('Ö','O'),('Ü','U')]

def convertToEng(twt):
	twt = str(twt)
	for tr, eng in ch:
		twt  = twt.replace(tr, eng)
	return twt

# Read groups
with open(filepath) as fp:
	line = fp.readline()
	while line:
		a = convertToEng(line).rstrip('\n').split(",")
		groups.append(a[0])
		length = len(a)
		keywords[a[0]]=a[1:length]
		line = fp.readline()


# Read tweets
#for line in open('./data/20180508132252', 'r'):
#	date = json.loads(line)["created_at"].split()
#	text = convertToEng(json.loads(line)["text"].encode("utf-8")).lower()
#	tweets.append(dict([("text", text),  ("group", "noGrp"), ("year", date[5]), ("month", date[1]), ("day", date[2])]))
#tweets.append(dict([("text", json.loads(line)["text"]), ("year", date[5]), ("month", date[1]), ("day", date[2])]))


################## -- Read tweets (path)
folder = "./data"

for file in os.listdir(folder):
	print(file)
	filepath = os.path.join(folder, file)
	for line in open(filepath, 'r'):
		date = json.loads(line)["created_at"].split()
		text = convertToEng(json.loads(line)["text"].encode("utf-8")).lower()
		tweets.append(dict([("text", text),  ("group", "noGrp"), ("year", date[5]), ("month", date[1]), ("day", date[2])]))


def mapFunc(x):
	for i in keywords.keys():
		for a in keywords[i]:
			if a in x['text']:
				x['group']= i
	del x['text']
	return x["group"] + "," + x["year"] + "," + x["month"] + "," + x["day"]



x = sc.parallelize(tweets)
y = x.map(lambda x: (mapFunc(x), 1)).reduceByKey(lambda x,y : x+y)

#y = x.map(lambda x: (mapFunc(x),1)).filter(lambda x: "group" in x[0]).reduceByKey(lambda a,b: a+b)
y = y.collect()

print(y)
data = []
for i in y:
	data.append(i[0].split(",")+[i[1]])

df = pd.DataFrame(data)
df = df[df[0] != "noGrp"]

print(df)

df.to_csv('out.csv')
