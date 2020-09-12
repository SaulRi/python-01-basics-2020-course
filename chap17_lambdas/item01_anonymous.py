
def my_own_calculus( number ):
    return  number * 3 + 1

print( f"The calculus of 5 is { my_own_calculus( 5 ) }" )
print( f"The calculus of 0 is { my_own_calculus( 0 ) }" )
print( f"The calculus of 15 is { my_own_calculus( 15 ) }" )


## we define an anonymous (lambda) expression
lambda  number: number * 3 + 1

## the analogy would be
"Some string"
25
True
print("All values were executed, but useless")


## Sample 1: let to rewrite the lambda
number_calculous = lambda number: number * 3 + 1

print( f" The calculous with lambda 5 is { number_calculous(5) } " )
print( f" The calculous with lambda 0 is { number_calculous(0) } " )
print( f" The calculous with lambda 15 is { number_calculous(15) } " )


##  Sample 2: get full name
get_full_name = lambda first_name ="", last_name= "":  first_name.strip().title() + " " + last_name.strip().title()

fName1 = get_full_name(  "   jUlio", "   VERNE " )
print( f" The fullname is { fName1 } " )


fName2 = get_full_name(  " Charles" )
print( f" The fullname is { fName2 } " )