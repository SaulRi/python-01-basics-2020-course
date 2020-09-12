## The range create a sequence of numbers
my_sequence =  range(1,6)
print( f"The type of my sequence is { type(my_sequence) } " )
print(  dir(my_sequence)  )
print()
print( f"my sequence is { my_sequence }" )
print( f"from range to list  {  list( my_sequence ) }" )
print( f"count 1 is { my_sequence.count(1)  }"  )
print( f"count 2 is { my_sequence.count(2)  }"  )
print( f"the sequence starts in { my_sequence.start  }"  )
print( f"the sequence stop in { my_sequence.stop  }"  )
print()


## basic
## From 1 to 10,  Open in first argument, close in the second one
basic_sequence = list( range(1, 11) )
print()

###
step2_sequence = list( range(  0, 13, 2) )
print( f"list two by two { step2_sequence }" )
print()

## 
minu1_sequence = list( range(  5, 0, -1) )
print( f"list minus 1 { minu1_sequence }" )
print()