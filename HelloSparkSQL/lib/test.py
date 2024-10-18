# file_path = 'spark.conf'

# with open(file_path, 'r') as file:
#     config_content = file.read()

# print(config_content)

import configparser

config = configparser.ConfigParser()

# Specify the path to your configuration file
config.read('spark.conf')

try:
    spark_app_name = config.items("SPARK_APP_CONFIGS")#['SPARK_APP_CONFIGS']['spark.app.name']
    print(f"App Name: {spark_app_name}")
except configparser.NoSectionError as e:
    print(f"Error: {e}")