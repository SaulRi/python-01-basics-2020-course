## Solve the error to show in console "Hasta la vista baby"
import sys
import os

sys.path.append( '../try_logger' )

from try_logger import logger

## Print hello world five times
for index in range( 5 ):
    print("Hello world")


## print the bye world 6 times
for index in range( 7 ):
    print("Bye world")


try :
    print("some code is try to be executed here")
except:
    logger.error("Something is wrong, solve it")    


print( "Hasta la vista baby 😎")