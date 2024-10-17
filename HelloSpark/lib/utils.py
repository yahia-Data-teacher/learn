import configparser
from pyspark import SparkConf

def get_spark_app_config():
    spark_conf = SparkConf()
    config = configparser.ConfigParser()
    config.read("spark.conf")

    for (key,val) in config.items("SPARK_APP_CONFIGS"):
        spark_conf.set(key,val)
    return spark_conf

def load_survey_df(spark, data_file):
    return spark.read.option("header",'true').option("inferSchema",'true').csv(data_file)

    # config.read('spark.conf')

    # try:
    #     spark_app_name = config.items("SPARK_APP_CONFIGS")#['SPARK_APP_CONFIGS']['spark.app.name']
    #     print(f"App Name: {spark_app_name}")
    # except configparser.NoSectionError as e:
    #     print(f"Error: {e}")