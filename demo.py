from lux_churn.logger import logging
from lux_churn.exception import LuxChurnException
import sys



logging.info("Logging has been initialized successfully.")

try:
    a=2/0
except Exception as e:
    raise LuxChurnException(e, sys)