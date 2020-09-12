## Mutate is change

colors = [ "red", "green", "blue", "black" , "white", "purple" ]
print( f"The elements in color array are {colors}")
print( f"The original size is { len(colors) }\n")

## modify by index
colors[2] = 'DARK BLUE'
print( f"The elements after modify blue are: {colors}\n")


## add elements one by one
colors.append("viiolet")
colors.append("magenta")
colors.append("pink")
print( f"The elements in color array  NOW are {colors}")
print( f"The new size after append is { len(colors) }\n")

## add multiple elements
colors.extend( ["yellow", "gray"] )
print( f"The elements after extend are {colors}")
print( f"The size after extend is { len(colors) }\n")

## add by index 
print( f"The colors previous insert {colors}")
index = colors.index("green")
print( f"The original index of green is { index }" )

colors.insert( 1, "orange" )
index = colors.index("green")
print( f"The colors after insert {colors}")
print( f"The new  index of green is {index }\n" )


## remove the last element by pop
poped_color = colors.pop()
print( f"The popeded color is {poped_color}" )
print( f"The list remains like {colors}\n" )

## remove by element
colors.remove("green")
print( f"The colors after remove green {colors}\n")

## What happend if we try to remove an item that does not exist in the list?
#colors.remove("green")

## delete all elements in the list
colors.clear()
print( f"The colors after remove all items {colors}\n")

## sorting
colors = [ "red", "green", "blue", "black" , "white", "purple" ]
print( f"Show the original items {colors}")

colors.sort()
print( f"The sorted items {colors}")
colors.sort( reverse=True )
print( f"The sorted in reverse order {colors}\n")

## Activity 1:  Add a new element at the end of the list color
