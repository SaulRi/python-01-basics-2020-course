from functools import reduce

## Very basic reduce sample
data = [ 2, 3,5,7, 11,13, 17, 19, 23, 29 ]

## Sample 1
multiplier = lambda acc, current: acc * current
result1 = reduce( multiplier, data, 1 )
print( f"Result of multiply is { result1 }" )

## Sample 2
adder = lambda acc, current : acc +  current
result2 = reduce( adder, data, 0 )
print( f"Result of add is { result2 }" )


## Activity 1 : Use for loop to get the result of multiply data list


## Activity 2 : Use while loop to get the result of adding the data list