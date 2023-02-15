from pyspark import SparkConf, SparkContextUsers
import collections

# here we actually create the Spark Context
    # we defined the local machine as the master node and in this 
        # example there's only 1 thread and doesn't have any sort of distribution
    # the app name is used to identify the application running
    # once configured, we can start the spark context
conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)

# reads the text file
lines = sc.textFile("file:///apache-spark-hands-on/activity-1-ml-100k-movies-lens/ml-100k")

# gets the 3rd "column" after a line split (because the line is read as string)
ratings = lines.map(lambda x: x.split()[2])

# counts every unique value
result = ratings.countByValue()

# here's pure python, not a spark
sortedResults = collections.OrderedDict(sorted(result.items()))
for key, value in sortedResults.items():
    print("%s %i" % (key, value))
