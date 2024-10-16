from pyspark.sql import *
from lib.logger import Log4j



if __name__ == "__main__":
    # print("Starting Hello Spark.")
    
    spark =SparkSession.builder \
        .appName("Hello Spark") \
        .master("local[3]") \
        .getOrCreate()
    spark.sparkContext.setLogLevel("WARN")
    logger = Log4j(spark)

    logger.info("Starting HelloSpark")
    # Your processing code



    logger.info("Starting HelloSpark")
    spark.stop()

    