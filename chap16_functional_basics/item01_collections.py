
## import module collections and we create a Schema of our Data

import collections

Avenger = collections.namedtuple('Avenger',[
    'name', 
    'real_name', 
    'power_level',
    'is_active'
])

print( Avenger )

## creating our avenger collection

Avenger( name="Iron Man", real_name="Tony Stark"  )