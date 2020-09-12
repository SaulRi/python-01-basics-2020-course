## Asking for values and indexes in array

colors = [ "red", "green", "blue", "black" , "white", "purple" ]
print( f"The elements in color array are {colors}")

exists_red = "red" in colors
exists_violet = "violet" in colors

print( f"red exists in colors ? {exists_red}")
print( f"violet exists in colors ? {exists_violet}")

red_index = colors.index("red")
blue_index = colors.index("blue")

## What happend if ask for the index of element tha is not in the array ?
#violet_index = colors.index("violet")

print( f"The index of red is {red_index} and the index of blue is {blue_index}" )

