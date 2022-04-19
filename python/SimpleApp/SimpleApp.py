#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""SimpleApp.py"""
from pyspark.sql import SparkSession

logFile = "/Users/gaojunliang/opt/spark-3.0.1-bin-hadoop2.7/README.md"
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()
