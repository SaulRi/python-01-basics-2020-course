import logging

# Logger format
LOG_FORMAT = "%(levelname)s  %(asctime)s - %(message)s"

# basic configuration
logging.basicConfig( 
    filename="./logs/TryData.log", 
    format=LOG_FORMAT,
    level=logging.DEBUG,    
    filemode= 'w' )

## create the root logger
logger = logging.getLogger()
