from pyspark.sql import *
class Log4jr:
    def __init__(self,spark):
        # log4j = spark._jvm.org.apache.log4j
        # root_class = "guru.learningjournal.spark.examples"
        # conf = spark.sparkContext.getConf()
        # app_name = conf.get("spark.app.name")
        # self.logger = log4j.LogManager.getLogger(root_class +"."+"HelloSpark")
        log4j = spark._jvm.org.apache.log4j
        root_class = "guru.learningjournal.spark.examples"
        conf = spark.sparkContext.getConf()
        self.app_name = conf.get("spark.app.name")
        self.logger = log4j.LogManager.getLogger(f"{root_class}.{self.app_name}")
        # self.logger.info("Log4j initialized successfully")  # Ajout d'un message pour vérifier l'initialisation

    def warn(self,message):
        self.logger.warn(message)
    def get_app_name(self):
        return self.app_name

    def info(self,message):
        self.logger.info(message)

    def error(self,message):
        self.logger.error(message)

    def debug(self,message):
        self.logger.debug(message)