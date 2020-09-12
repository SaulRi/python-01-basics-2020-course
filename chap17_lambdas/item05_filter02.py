# Remove missing data
""" 
    Empty values in Python are
    "", 0, 0.0, [], (), {}, False, None
"""

country_list = [  "" , "Argentina", "Brazil", "Chile", "Colombia", "Ecuador", "", "" , "Venezuela", ""  ]
print( f"Original List is { country_list}" )
print()

## 'Special' case in Python
not_empty = list( filter( None, country_list) )
print( f"Clean List is { not_empty }" )

