from pyspark.sql import *
# import os
if __name__ == "__main__":
    #print("helloSpark")
    # os.environ["PYSPARK_PYTHON"] ="C:/Users/yahia/AppData/Local/Programs/Python/Python312-32/python.exe"
    spark = SparkSession.builder\
            .appName('Hello Spark')\
            .master("local[2]")\
            .getOrCreate()

    data_list = [('Ravi',28),
                 ('David',45),
                 ('Abdul',37)]

    df = spark.createDataFrame(data_list).toDF('Name','Age')
    df.show()
    spark.stop()