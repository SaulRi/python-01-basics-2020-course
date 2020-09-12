
def greet():
    print("Hello world")


def sayBye( name="John" ):
    print(f"Bye bye {name}")

greet()
greet()

print()

sayBye("Leo")
sayBye("Diego")
sayBye()

# The function is void , dont return any value
# send error
#get_void = sayBye()

print()

def my_sum( number1, number2 ):
    return number1 + number2

result1 = my_sum(5, 4)
result2 = my_sum(3, 100)

print( f"5+4 = {result1} and 3 + 100 = {result2} " )