#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys, json
import pandas as pd
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

#os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3'

conf = SparkConf()
sc = SparkContext(conf = conf)

keywords={} # group : keys (Dict)
groups = [] # groups
tweets = [] # text, year, month, day

filepath = 'keywords-groups.txt'

ch = [('ç','c'),('Ç','C'),('ı','i'),('İ','I'),('ğ','g'),('Ğ','G'),('ü','u'),('ö','o'),('Ş','S'),('ş','s'),('Ö','O'),('Ü','U')]

# Replace all characters with English characters.
def convertToEng(str):
	str = str(str)
	for tr, eng in ch:
		str  = str.replace(tr, eng)
	return  str

# Read groups
with open(filepath) as fp:
	line = fp.readline()
	while line:
		a = convertToEng(line).rstrip('\n').split(",")
		groups.append(a[0])
		length = len(a)
		keywords[a[0]]=a[1:length]
		line = fp.readline()


# Tweets path
folder = sys.argv[1] #"./data"


# Map Function
def mapFunc(line):
	date = json.loads(line)["created_at"].split()
	text = convertToEng(json.loads(line)["text"].encode("utf-8")).lower()
	x = dict([("text", text),  ("group", "noGrp"), ("year", date[5]), ("month", date[1]), ("day", date[2])])

	for i in keywords.keys():
		for a in keywords[i]:
			if a in x['text']:
				x['group']= i
	del x['text']
	return x["group"] + "," + x["year"] + "," + x["month"] + "," + x["day"]



data = sc.textFile(folder, use_unicode=False)

y = data.map(lambda line: (mapFunc(line),1)).reduceByKey(lambda x,y : x+y)
y = y.collect()

print(y)
data = []
for i in y:
	data.append(i[0].split(",")+[i[1]])

df = pd.DataFrame(data)
df = df[df[0] != "noGrp"]


# save results to out.csv file
df.to_csv('out.csv')
