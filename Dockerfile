# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set environment variables for Spark and Hadoop
ENV SPARK_VERSION=3.5.3
ENV HADOOP_VERSION=3.3.1
ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3

# Install dependencies including Git
RUN apt-get update && apt-get install -y \
    openjdk-17-jre-headless \
    wget \
    procps \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Hadoop
RUN wget -q https://archive.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz \
    && tar -xzf hadoop-${HADOOP_VERSION}.tar.gz -C /opt/ \
    && rm hadoop-${HADOOP_VERSION}.tar.gz

# Install Spark
RUN wget -q https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.tgz \
    && tar -xzf spark-${SPARK_VERSION}-bin-hadoop3.tgz -C /opt/ \
    && rm spark-${SPARK_VERSION}-bin-hadoop3.tgz

# Set environment variables for Spark and Hadoop
ENV HADOOP_HOME=/opt/hadoop-${HADOOP_VERSION}
ENV SPARK_HOME=/opt/spark-${SPARK_VERSION}-bin-hadoop3
ENV PATH=$PATH:$SPARK_HOME/bin:$HADOOP_HOME/bin

# Install PySpark and Jupyter
RUN pip install pyspark jupyter

# Set working directory
WORKDIR /app

# Expose the Jupyter port
EXPOSE 8888