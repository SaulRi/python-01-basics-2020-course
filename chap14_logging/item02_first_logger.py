import os
import logging

# Define log file
log_path = './logs/Data.log'

## create directory and log file
os.makedirs( os.path.dirname( log_path ), exist_ok=True )


# String format for the messages
LOG_FORMAT = "%(levelname)s  %(asctime)s - %(message)s"

## Create and configure logger
## The default level is WARNING
## The default filemode is a (from append), if you want a new one use w (write)
logging.basicConfig( 
    filename=log_path, 
    format=LOG_FORMAT,
    level=logging.DEBUG,    
    filemode= 'a' )

## create root logger
logger = logging.getLogger()

# Message from application
print( f"Logger lever is { logger.level }")

## Test all levels 
logger.debug("This is for traicing events...")
logger.info('Useful message or event happend')
logger.warning('Checkit out.. something could be wrong.. not yet, but soon!!  ')
logger.error("Your application is failing and you have to fixit  😥   ")
logger.critical("The entire internet is down, the hell is burning  🔥")

