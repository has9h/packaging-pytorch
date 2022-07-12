# -*- coding: utf-8 -*-

from os import path
from datetime import datetime
from collections import ChainMap
from logging.handlers import RotatingFileHandler

import os
import sys
import json
import time
import logging

try:
    import cv2
    print(cv2.__file__)
    print('Successfully loaded cv2')
    try:
        import easyocr
        print('Successfully loaded easyocr')
    except Exception as ocr_err:
        print('easyocr failed to bundle')
except Exception as e:
    print('Error bundling cv2')
    print(e)

try:
    reader = easyocr.Reader(['en'], gpu=False)   
    # Custom logger
    logger = logging.getLogger(__name__)

    # Create handler for logs
    # Remember to manually create the directory
    handler = RotatingFileHandler(path.join(path.abspath('logs'), logger.name), mode='a', maxBytes=10000, backupCount=10)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.debug('OCR script running')
except Exception as e:
    print(e)



input('Here to wait.')