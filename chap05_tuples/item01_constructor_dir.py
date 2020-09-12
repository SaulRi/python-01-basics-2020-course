## Think in tuples like constants


## Most common way to create tupple
common_tupple = ( 1, 2, 3, 5, 5 )

## usgin the "constructor"
constructor_tupple = tuple( ("a", "b", "c") )

## samples o tupples

# tupple of string
colors_tupple = ( "red", "green", "list" )

# tupple of booleans
boolean_tuple = ( True, False, True, True, False )

# tupple fo any 
any_tuple = ( 1,2,4 , False, "something", [  12, 34, 5 ]  )


##
not_tuple = ( 1 )
print(  f"value of not_tuple {not_tuple} and its type { type(not_tuple)  } " )

## the comma is important to create tuples
tupple_of_one = ( 1, )
print(  f"value of tuple of one {tupple_of_one } and its type { type( tupple_of_one )  } " )



print( dir( any_tuple )  )