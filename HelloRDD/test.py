import logging

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO)

# Replace logger = Log4j(spark) with a simple logger
logger = logging.getLogger(__name__)