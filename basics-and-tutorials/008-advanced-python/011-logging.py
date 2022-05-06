# logging

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s')
logger = logging.getLogger("test_logger")

logger.info('This will not show up.')
logger.warning('This will')
logger.debug('Sample for debug log')
logger.critical('Bad stuff')

"""
DEBUG - not showed by default
INFO - not showed by default
WARNING
ERROR
CRITICAL
"""