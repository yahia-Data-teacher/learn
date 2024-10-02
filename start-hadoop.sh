#!/bin/bash

# Format HDFS (first time only)
hdfs namenode -format

# Start HDFS
start-dfs.sh

# Start YARN
start-yarn.sh

# Optionally: Start Spark
