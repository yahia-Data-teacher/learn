from pyspark.sql import SparkSession

from lib.logger import Log4j

if __name__=="__main__":
    spark = SparkSession \
        .builder \
        .master("local[3]") \
        .appName("SparkSchemaDema") \
        .getOrCreate()
    spark.sparkContext.setLogLevel("INFO")
    logger = Log4j(spark)

    flightTimeCsvDF = spark.read \
        .format("csv") \
        .option("header","true") \
        .load("data/flight*.csv")

    flightTimeCsvDF.show(5)
    logger.info("CSV Schema:" + flightTimeCsvDF.schema.simpleString())

    flightTimeJsonDF = spark.read \
        .format("json") \
        .load("data/flight*.json")

    flightTimeJsonDF.show(5)
    logger.info("Json Schema:" + flightTimeJsonDF.schema.simpleString())

    flightTimeParquetDF = spark.read \
        .format("json") \
        .load("data/flight*.parquet")

    flightTimeJsonDF.show(5)
    logger.info("Parquet Schema:" + flightTimeJsonDF.schema.simpleString())