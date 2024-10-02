FROM gitpod/workspace-full:latest

# Install Hadoop, YARN, Spark, and Jupyter
RUN sudo apt-get update && \
    sudo apt-get install -y hadoop spark jupyter && \
    apt-get clean

# Set up Hadoop environment variables
ENV HADOOP_HOME=/usr/local/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin

# Set up Spark environment variables
ENV SPARK_HOME=/usr/local/spark
ENV PATH=$PATH:$SPARK_HOME/bin

# Install Python dependencies
RUN pip install pyspark
