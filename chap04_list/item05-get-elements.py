## Get elements in array

colors = [ "red", "green", "blue", "black" , "white", "purple" ]
print( f"The elements in color array are {colors}")
size = len( colors )

print(f"The size of color array is {size}")
'''
to access an specific element, 
we use their position in the array and brackets
'''

print( f"The item in index 0 : { colors[0] }" )
print( f"The item in index 1 : { colors[1] }" )
print( f"The item in index 2 : { colors[2] }" )

#What happen when use an index with value equals to size?
#print( f"The element in index equals to size  {colors[ size ]  } "  )

print( f"The last element, where index is size -1 ( {size -1} ) : {colors[ size -1 ]  } "  )


# what will happend with negative indexex
print( f"The item in index -1 : { colors[ -1 ] }" )
print( f"The item in index -2 : { colors[ -2 ] }" )
print( f"The item in index -5 : { colors[ -5 ] }" )
print( f"The item in index -6 : { colors[ -6 ] }" )

## What happend when index is lower than first position?
#print( f"The item in index -7 : { colors[ -7 ] }" )


## Activity..