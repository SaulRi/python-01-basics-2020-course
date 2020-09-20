# Third party modules

"""
Check https://pypi.org/
Install  colorama by pip or pip3
"""

from colorama import Fore, Style, init
import platform

my_system = platform.system()

## this is a ternary if
is_windows = True if my_system == 'Windows' else False

# Use convert True for windows systems
init( convert=is_windows )


print( f"My system is {my_system}")

print( "Hello world a secas..")
print( Fore.YELLOW +  "Hello YELLOW world")
print( Fore.RED , "Hello RED world")
print( f"{Fore.BLUE} Hello BLUE world " )
