from colorama import Fore, Style, init
import platform

my_system = platform.system()
## this is a ternary if
is_windows = True if my_system == 'Windows' else False
# Use convert True for windows systems
init( convert=is_windows )


csv_path = 'google_stock_data.csv'
csv_file = open( csv_path )
size = 0

for line in csv_file:
    print(  f"{Fore.GREEN} {line}" )
    size+=1

print( f"\nTotal lines are {  size  }" )