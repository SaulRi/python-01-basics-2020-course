##  we can define a function

def add_one(number):
    """
    THis function get a number and increments the value in one
    :param str number: The number to be incremented
    :return: The number plus one
    """
    return number + 1

print( f"Our funciton is {add_one}" )
print(  add_one(1) )
print(  add_one(2) )
print(  add_one(3), "\n" )


def sayHello(name):
    """ 
    Just a hello function
    :param str name: The name in the function   
    :return: The concatenated string to say hello and the name
    """
    return f"Hello {name}"

print( f"Our hello function is {sayHello }")
print(  sayHello("Ringo") )    
print(  sayHello("Tony") )    
print(  sayHello("Leo"), "\n" ) 


def sayBye(name="Baby"):
    """ 
    Just a bye function
    :param str name: The name in the function   
    :return: The concatenated string to say hello and the name
    """
    return f"Hasta la vista {name}"




"""
First class object, is an entity dynamically created, destroy.
it means there are no restrictions on the object's use. It's the same as any other objec
"""

#Assign a funtion to a variable
first_class_obj = add_one

print( f"First class is {first_class_obj}\n"  )
print( first_class_obj(10) )


#Assigne two o more funcions in a list

## we can store functions in a list
execution_list = [ add_one, sayHello ]
print( f"first item is { execution_list[0] }"  )
print( f"second item is { execution_list[1] }"  )

# and can execute each function
print( f"Execution first item: { execution_list[0](50)   }"  )
print( f"Execution of second item is { execution_list[1]( 'Peter' ) }\n"  )


## pass a function like argument of a function

def get_functions( function01, function02  ):
    """ This function received two functions  """
    
    ## those arguments are callable objects
    function01()
    function02()


f01 = lambda : print("Hello World")
f02 = lambda : print("Good By")
print( f"The type of f01 is { type(f01) } and the type of f02 { type(f02) } \n" )
get_functions( f01, f02 )
print()


def execute( some_function  ):
    return some_function("Daniel San")

answer1 = execute( sayHello )
answer2 = execute( sayBye )

print( f"The answer1 of sending sayHello is {answer1}"  )
print( f"The answer2 of sending sayBay is {answer2}  \n"  )