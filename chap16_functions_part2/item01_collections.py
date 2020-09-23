
## import module collections and we create a Schema of our Data

import collections

Avenger = collections.namedtuple('Avenger',[
    'name', 
    'real_name', 
    'power_level',
    'is_active'
])

print( Avenger )

## creating our avenger 
iron_man =  Avenger( name="Iron Man", real_name="Tony Stark", power_level=100, is_active=True  )
print( iron_man )
print( f"name is { iron_man.name }" )

# We get an error, if we try to change data
#iron_man.name = "War Machine"

iron_man =  Avenger( name="Iron Man", real_name="Tony Stark", power_level=100, is_active=True  )
capitian_america =  Avenger( name="Capitain America", real_name="Steve Rogers", power_level=500, is_active=True  )
thor =  Avenger( name="Thor", real_name="Thor Odin's Son", power_level=1000, is_active=False  )

## we are mixing mutable with inmutable data, we can modify the list
avenger_list = [  iron_man, capitian_america, thor ]
print( f"Avenger.. assemble {avenger_list}\n" )

## we can add more Avengers
avenger_list.append(  Avenger( name="Hawk Eye", real_name="Clint Barton", power_level=50, is_active=True  ) )
print( f"Avenger list with HawK Eye...{avenger_list}\n" )

## or set any other thing
avenger_list.extend( [ 45, False, "Fantastic Four"  ] )
print( f"Avenger with.. anything else {avenger_list}\n" )