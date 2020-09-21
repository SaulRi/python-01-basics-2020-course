
from try_logger import logger

# 
try:
    logger.info( "Result {0} / {1}".format( 5, 0 )   )
    print( f"Result 5 /0 = { 5/0 }" )
except:
    logger.error( "something is wrong" )


try:
    logger.info( f"Info with String interpolations {6} / {0}" )
    print( f"Result 6 /0 = { 6/0 }" )
except Exception as err:    
    logger.error( f"Error is: {err}" )


print("\nThe program ALWAYS ends")