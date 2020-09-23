from colorama import Fore, Style, init
import platform
import collections

my_system = platform.system()
is_windows = True if my_system == 'Windows' else False
init( convert=is_windows )

Avenger = collections.namedtuple('Avenger',[
    'name', 
    'real_name', 
    'power_level',
    'is_active'
])


## creating our avengers
iron_man =  Avenger( name="Iron Man", real_name="Tony Stark", power_level=100, is_active=True  )
capitian_america =  Avenger( name="Capitain America", real_name="Steve Rogers", power_level=500, is_active=True  )
thor =  Avenger( name="Thor", real_name="Thor Odin's Son", power_level=1000, is_active=False  )
hawk_eye = Avenger( name="Hawk Eye", real_name="Clint Barton", power_level=50, is_active=True  ) 
black_widow =  Avenger( name="Black Widow", real_name="Natasha Romanov", power_level=70, is_active=False  )

assemble = (  iron_man, capitian_america, thor, hawk_eye, black_widow  )


print( f"{Fore.RED} Iron Man : { assemble[0] } "  )
print( f"{Fore.BLUE} Captain America : { assemble[1] } "  )
print( f"{Fore.YELLOW} Thor : { assemble[2] } "  )
print( f"{Fore.GREEN } Hawk Eye : { assemble[3] } "  )
print( f"{Fore.LIGHTBLACK_EX} Black Widow : { assemble[4] } "  )

