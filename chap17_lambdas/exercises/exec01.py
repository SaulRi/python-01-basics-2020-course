# with map and lambda transform the array data from celcious to farenheit
celcius_list = [  
    ( "Berlin",  29 ),( "Cairo",  36 ),( "Buenos Aires",  19 ),
    ( "Los Angeles",  26 ),( "Tokyo",  27 ),( "New York",  28 ),
    ( "London",  22 ),( "Beijin",  32 )
]
print( f"Celcius list { celcius_list }"  )
print()

"""
 Formula is   F = 9/5* C + 32
"""
get_farenheit =  lambda  data_tup: ( data_tup[0], (9/5)*data_tup[1] + 32 )

farenheit_list = list( map( get_farenheit, celcius_list ) )
print( f"Farenheit list { farenheit_list }" )