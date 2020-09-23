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
print( f"Execution of second item is { execution_list[1]( 'Peter' ) }"  )


## pass a function like argument of a function



