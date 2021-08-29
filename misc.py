import logging
import random
import string
import time
from logging.handlers import TimedRotatingFileHandler


def now_sec():
    return int(time.time())


def now_ms():
    return int(time.time() * 1000)


def gen_guid():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(10))


def get_logger(loggerName):
    logfilePath = f"{loggerName}.log"
    myLogger = logging.getLogger(loggerName)
    myLogger.setLevel(logging.INFO)
    fileHandler = TimedRotatingFileHandler(logfilePath, when='midnight', interval=1, backupCount=7, encoding='utf8')
    logFormatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fileHandler.setFormatter(logFormatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(logFormatter)
    streamHandler.setLevel(logging.WARNING)
    myLogger.propagate = False
    # myLogger.addHandler(streamHandler)
    myLogger.addHandler(fileHandler)
    return myLogger
