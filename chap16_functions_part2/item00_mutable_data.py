
"""
One principle say the data must be inmutable. But lets see...
"""

# First: We can get a typo error, in attribute nami instead of name in Thor
avenger_list =[
    { "name": "IronMan", "real_name" : "Tony Stark", "power_level": 100, "is_active": True  },
    { "name": "Capitain America", "real_name" : "Steave Rogers", "power_level": 300, "is_active": True  },
    { "nami": "Thor", "real_name" : "Thor Odin's Son", "power_level": 500, "is_active": False  }
]    

print ( f"Avenger  are {avenger_list} and  number of avenger is { len(avenger_list) } \n" )


# we chan modify the list
del avenger_list[1]

# we chan change data in the list
avenger_list[ 0 ]['name'] = "War Machine"

print ( f"FinallyAvenger  are {avenger_list} and  number of avenger is { len(avenger_list) }" )
