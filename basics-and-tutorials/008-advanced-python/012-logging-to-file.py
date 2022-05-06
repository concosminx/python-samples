import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt')


logger = logging.getLogger('my_app')
logger.debug("This is a debug log")
logger.info("This is an info log")
logger.critical("This is critical")
logger.error("An error occurred")


# import logging
#
# logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
#     datefmt='%d-%m-%Y:%H:%M:%S',
#     level=logging.DEBUG,
#     filename='logs.txt')
#
# logger = logging.getLogger('my_app')
#
# another_logger = logging.getLogger('my_app.database')  # gets a child logger called 'database' of 'my_app'
