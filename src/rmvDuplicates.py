from pyspark import SparkConf, SparkContext
import sys, os, json, datetime
from operator import add
from pyspark.sql import SparkSession
os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3'

conf = SparkConf()
sc = SparkContext(conf = conf)


def mapFunc(line):
        tweet = json.loads(line)['id']
        return tweet

def redFunc(line1, line2):
	return line2

inputPath = "./data/"
input = sc.textFile(inputPath)

output = input.map(lambda x: (mapFunc(x),x)).reduceByKey(lambda x,y: redFunc(x,y))

outputPath = "./data2/"
output.saveAsSequenceFile(outputPath)
