<div style="text-align: center;">
<h1>Apache Spark Hands On</h1>
<h2>
    <a href="https://www.udemy.com/course/taming-big-data-with-apache-spark-hands-on" target="_blank">A Udemy Course</a>
</h2>
</div>

# Course Overview


- Use Apache Spark to analyze massive data sets;
- 15 Hands On Projects;
- Run locally and in the cloud (with AWS EMR);
- Analyze 1 million movie ratings and produce movies that are similar to each other;
- Uses Python.


# Important Notes

- Don't install Java 16 if JDK aren't installed yet in your PC;
- Apache Spark is only compatible with Java 8 or Java 11.


# Getting Set Up
## Python
Install Python 3+.
## JDK
Install JDK 8 (not newer)
&#9888;Watch out: the path must not contain spaces!!
## Spark
Install Spark 2+
&#9888;Watch out: change the <i>log4j.properties.template</i> file name to <i>log4j.properties</i>
&#9888;Watch out: inside <i>log4j.properties</i>, set the log level for <b>error</b>, instead <b>info</b>.
&#9888;Watch out: if you are on WINDOWS, download <i>winutils.exe</i>

## MovieLens
Download the Movie Lens 100k data set

# Activity 1 - Ratings Histogram

# Introduction do Spark

## What's Spark?
A fast and general engine for large-scale data processing

## How it's scalable?
There's a Driver Program (Spark Context) that manages the program/script you want to run, but under the hood, it manages some task in some nodes.
It's possible because there's an architecture, mainly the Cluster Manager, that execute, distribute and store metadata about the nodes (YARN). It's based on horizontal scalability.

## It's fast
Run programs up to 100x faster than Hadoop MapReduce in memory, or 10x faster on disk.
DAG Engine (Directed Acyclic Graph) optimizes workflows.

## Is not that hard
Code in Python, Java, or Scala.
Built around one main concept: Resilient Distributed Dataset.

## Components of Spark

- Spark Streaming
- Spark SQL
- MLLib
- GraphX


# RDD
## What's it?
The Resilient Distributed Dataset, as known as RDD, is the core object in Spark, because everything (or almost it) relays on it.
Fundamentally it's dataset, and it's an abstraction for a giant set of data distributed among many nodes on a cluster.
It's able to handle the failure of specific executor nodes in your cluster automatically and keep on going even if one node shuts down.

## SparkContext object
It's created by your driver program and it's responsible for making RDD's resilient and distributed, because it manages the meta data os the data nodes.
Also creates RDD's. The Spark shell creates a "sc" object for you.

## Creating RDD's
It's possible to create RDD's with some methods given by Spark Context:

- parallelize(list)
- sc.textFile("file_path.txt")
- HiveContext(sc).sql(SQL query)
- Can also create from:
    - JDBC
    - Cassandra
    - HBase
    - ElasticSearch
    - JSON, CSV, sequence files, object, compressed formats, etc...

## Transforming RDD's
There's some operations that gives some ways to shape of form the datasets:

- map: "iterate" over every item, passing the value as a parameter to a function, returning another value.
- flatmap: very similar to the previous, but it can produce multiple values.
- filter: used to select specific itens that contains certain value
- distinct: selects only the unique values of a set
- sample: selects just a sample of the data. Very useful for testing.
- union, intersection, subtract, cartesian...: combines two differentes RDD's with different ways.

## Lazy Evaluation
Nothing actually happens in your driver program until an action is called.

## Key/Value RDD's and the Average Friends by Age Example
RDD's can hold key/value pairs, like Pandas DataFrame.
There're some methods used for key/value pairs data, like:

- reduceByKey(): combine values with the same key using some function.
    ```python
    rdd.reduceByKey(lambda x, y: x + y)
    ```
- groupByKey(): group values with the same key.
- sortByKey(): sort RDD by key values.
- keys(), values(): create an RDD of just the keys, or just the values.

Imagine an input .txt data:
> ID,name,age,number of friends

> 0,Will,33,385
> 1,Jean-Luc,33,2
> 2,Hugh,55,221
> 3,Deanna,40,465
> 4,Quark,68,21

To return key/value pairs of age and number of friends:

```python
def parseLine(line):
    fields = line.split(',')
    age = int(fields[2])
    numFriends = int(fields[3])

    return (age, numFriends)

lines = sc.textFile("path_file.csv")
rdd = lines.map(parseLine)
```

