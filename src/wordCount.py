from pyspark import SparkConf, SparkContext
import sys
from operator import add
from pyspark.sql import SparkSession
conf = SparkConf()
sc = SparkContext(conf = conf)

input = sc.textFile("Sample.txt")
counts = input.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(add)
output = counts.collect()
for (word, count) in output:
	print("%s: %i" % (word, count))
