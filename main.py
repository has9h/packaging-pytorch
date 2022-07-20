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

# Custom logger
logger = logging.getLogger(__name__)

# Create handler for logs
# Remember to manually create the directory
handler = RotatingFileHandler(path.join(path.abspath('logs'), logger.name), mode='a', maxBytes=10000, backupCount=10)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

try:
    import cv2
    logger.debug('Successfully loaded cv2')
    print('Successfully loaded cv2')
    try:
        import easyocr
        logger.debug('Successfully loaded easyocr')
        print('Successfully loaded easyocr')
    except Exception as OCRImportError:
        print('Error importing easyocr', OCRImportError)
        logger.error('Error importing easyocr')
        logger.error(OCRImportError)
except Exception as CV2Error:
    print('Error importing cv2', CV2Error)
    logger.error('Error importing cv2')
    logger.error(CV2Error)


try:
    reader = easyocr.Reader(['en'], gpu=False)

    print('OCR script running')
    logger.debug('OCR script running')

    # Storing the stream value in a variable
    streamInJSONFormat = sys.argv[1]
    try:
        streamInDictionaryFormat = json.loads(streamInJSONFormat)
        logger.info("VSM")
        logger.info(streamInDictionaryFormat["bedId"])
        
        print('VSM')
        print(streamInDictionaryFormat["bedId"])
    except Exception as JSONParseError:
        print('Error parsing', JSONParseError)
        
        logger.error(f'Error parsing {streamInDictionaryFormat}')
        logger.error(JSONParseError)
except Exception as OCRError:
    print('Error reading OCR object', OCRError)
    
    logger.error('Error reading OCR object')
    logger.error(OCRError)

input('Here to wait.')
