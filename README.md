<h1 align="center">Apache Spark Hands On</h1>
<a href="https://itau.udemy.com/course/taming-big-data-with-apache-spark-hands-on/" target="_blank"><h2 align="center" style= "color: navy; text-decoration: underline">A Udemy Course</h2></a>

<h1>Course Overview</h1>

<ul>
<li>Use Apache Spark to analyze massive data sets;</li>
<li>15 Hands On Projects;</li>
<li>Run locally and in the cloud (with AWS EMR);</li>
<li>Analyze 1 million movie ratings and produce movies that are similar to each other;</li>
<li>Uses Python.</li>
</ul>

<h1>Important Notes</h1>
<ul>
<li>Don't install Java 16 if JDK aren't installed yet in your PC;</li>
<li>Apache Spark is only compatible with Java 8 or Java 11.</li>
</ul>

<h1>Getting Set Up</h1>
<h2>Python</h2>
<p>Install Python 3+.</p>
<h2>JDK</h2>
<p>Install JDK 8 (not newer)</p>
<p>&#9888;Watch out: the path must not contain spaces!!</p>
<h2>Spark</h2>
<p>Install Spark 2+</p>
<p>&#9888;Watch out: change the <i>log4j.properties.template</i> file name to <i>log4j.properties</i></p>
<p>&#9888;Watch out: inside <i>log4j.properties</i>, set the log level for <b>error</b>, instead <b>info</b>.</p>
<p>&#9888;Watch out: if you are on WINDOWS, download <i>winutils.exe</i></p>

<h2>MovieLens</h2>
<p>Download the Movie Lens 100k data set</p>

<h1>Activity 1 - Ratings Histogram</h1>

<h1>Introduction do Spark</h1>

<h2>What's Spark?</h2>
<p>A fast and general engine for large-scale data processing</p>

<h2>How it's scalable?</h2>
<p>There's a Driver Program (Spark Context) that manages the program/script you want to run, but under the hood, it manages some task in some nodes.</p>
<p>It's possible because there's an architecture, mainly the Cluster Manager, that execute, distribute and store metadata about the nodes (YARN). It's based on horizontal scalability.</p>

<h2>It's fast</h2>
<p>Run programs up to 100x faster than Hadoop MapReduce in memory, or 10x faster on disk.</p>
<p>DAG Engine (Directed Acyclic Graph) optimizes workflows.</p>

<h2>Is not that hard</h2>
<p>Code in Python, Java, or Scala.</p>
<p>Built around one main concept: Resilient Distributed Dataset.</p>

<h2>Components of Spark</h2>
<ul>
<li>Spark Streaming</li>
<li>Spark SQL</li>
<li>MLLib</li>
<li>GraphX</li>
</ul>

<h1>RDD</h1>
