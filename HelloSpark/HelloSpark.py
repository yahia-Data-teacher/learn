from pyspark.sql import *
from lib.logger import Log4j
import os
# Define the log file directory and name
log_directory = "/workspace/learn/app-log"  # Change to your desired path
log_file_name = "Hello-Spark.log"

# Ensure the directory exists
os.makedirs(log_directory, exist_ok=True)

if __name__ == "__main__":
    # print("Starting Hello Spark.")
    #spark.stop()
    print(os.getcwd())
    spark =SparkSession.builder \
        .appName("Hello Spark") \
        .master("local[3]") \
        .config("spark.executor.extraJavaOptions", "-Dlog4j.configuration=file:/workspace/learn/HelloSpark/log4j.properties") \
        .config("spark.driver.extraJavaOptions", "-Dlog4j.configuration=file:/workspace/learn/HelloSpark/log4j.properties") \
        .getOrCreate()
    
    # Change le niveau de log après l'initialisation
    spark.sparkContext.setLogLevel("WARN")
    logger = Log4j(spark)  # Initialise le logger
    
    
    
    # Log pour vérifier l'initialisation
    # logger.info("Log4j initialized successfully")
    
    logger.info("Starting application...")


    # try:

    #     logger.info("Starting HelloSpark")
    #     logger.info("Before starting HelloSpark")
    #     logger.info("Starting HelloSpark")
    #     logger.info("After starting HelloSpark")

    #     # Your processing code here
    # except Exception as e:
    #     logger.error(f"An error occurred: {e}")
    #     print(f"An error occurred: {e}")

    # Your processing code



    logger.info("Application completed successfully")
    
    spark.stop()
    #spark.stop()

    