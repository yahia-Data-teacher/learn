from pyspark.sql import SparkSession

class Log4j:
    def __init__(self, spark):
        log4j = spark._jvm.org.apache.log4j
        conf = spark.sparkContext.getConf()
        self.app_name = conf.get("spark.app.name")
        root_class = f"{self.app_name}.logger"
        self.logger = log4j.LogManager.getLogger(root_class)
        print(f"Log4j initialized for application: {self.app_name}")

    def warn(self, message):
        self.logger.warn(message)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)
