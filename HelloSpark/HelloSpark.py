from pyspark.sql import *
from pyspark import SparkConf
from lib.logger import Log4j
from lib.utils import *
import os
import sys
# Define the log file directory and name
log_directory = "/workspace/learn/app-log"  # Change to your desired path
log_file_name = "Hello-Spark.log"

# Ensure the directory exists
os.makedirs(log_directory, exist_ok=True)

if __name__ == "__main__":
    # print("Starting Hello Spark.")
    #spark.stop()
    conf = get_spark_app_config()
    # print(os.getcwd())
    spark =SparkSession.builder \
        .config(conf=conf) \
        .getOrCreate()
        # .appName("Hello Spark").master("local[3]")
        # .config("spark.executor.extraJavaOptions", "-Dlog4j.configuration=file:/workspace/learn/HelloSpark/log4j.properties") \
        # .config("spark.driver.extraJavaOptions", "-Dlog4j.configuration=file:/workspace/learn/HelloSpark/log4j.properties") \
    
    # Change le niveau de log après l'initialisation
    spark.sparkContext.setLogLevel("INFO")
    logger = Log4j(spark)  # Initialise le logger
    
    if len(sys.argv) != 2:
        # print(sys.argv)
        logger.error("Usage: HelloSpark <filename>")
        sys.exit(-1)
    
    # Log pour vérifier l'initialisation
    # logger.info("Log4j initialized successfully")
    
    # logger.info("Starting application...")


    # try:

    logger.info("Starting HelloSpark")
    # logger.info("After starting HelloSpark")
    # conf_out = spark.sparkContext.getConf()
    survey_df = load_survey_df(spark,sys.argv[1])
    partitioned_survey_df = survey_df.repartition(2)
    count_df = count_by_country(partitioned_survey_df)
    logger.info(count_df.collect())

    input('press Enter')
           # Your processing code here
    # except Exception as e:
    #     logger.error(f"An error occurred: {e}")
    #     print(f"An error occurred: {e}")

    # Your processing code



    #logger.info(conf_out.toDebugString())
    logger.info("Application completed successfully")
    
    # spark.stop()
    spark.stop()

    