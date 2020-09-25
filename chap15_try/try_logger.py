import logging
import os

# Define log file
log_path = './logs/TryData.log'

## create directory and log file
os.makedirs( os.path.dirname( log_path ), exist_ok=True )


# Logger format
LOG_FORMAT = "%(levelname)s  %(asctime)s - %(message)s"

# basic configuration
logging.basicConfig( 
    filename=log_path, 
    format=LOG_FORMAT,
    level=logging.DEBUG,    
    filemode= 'a' )

## create the root logger
logger = logging.getLogger()
