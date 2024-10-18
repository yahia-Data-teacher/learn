import logging
from pyspark import SparkConf
from pyspark.sql import SparkSession
import sys
from lib.logger import Log4j
from collections import namedtuple

SurveyRecord = namedtuple("SurveyRecord", ["Age", "Gender", "Country", "State"])

# Configure logging
logging.basicConfig(level=logging.ERROR)  # Suppress most logs
logger = logging.getLogger('logger')  # Adjust to your logger name
logger.setLevel(logging.INFO)  # Set the level to INFO for your logger

if __name__ == '__main__':
    conf = SparkConf() \
        .setMaster("local[3]") \
        .setAppName("HelloRDD")

    spark = SparkSession.builder \
        .config(conf=conf) \
        .getOrCreate()

    sc = spark.sparkContext
    sc.setLogLevel("INFO")  # Set Spark logging level to ERROR to suppress logs

    logger = Log4j(spark)  # Initialize your logger

    if len(sys.argv) != 2:
        logger.error("Usage: HelloSpark <filename>")
        sys.exit(-1)

    linesRDD = sc.textFile(sys.argv[1])
    header = linesRDD.first()
    linesRDD = linesRDD.filter(lambda line: line != header)

    partitionrdRDD = linesRDD.repartition(2)
    colsRDD = partitionrdRDD.map(lambda line: line.replace('"', '').split(","))
    selectRDD = colsRDD.map(lambda cols: SurveyRecord(int(cols[1]), cols[2], cols[3], cols[4]))
    filteredRDD = selectRDD.filter(lambda r: r.Age < 40)

    kvRDD = filteredRDD.map(lambda r: (r.Country, 1))
    countRDD = kvRDD.reduceByKey(lambda v1, v2: v1 + v2)

    colsList = countRDD.collect()

    for x in colsList:
        logger.info(x)  # Log the results