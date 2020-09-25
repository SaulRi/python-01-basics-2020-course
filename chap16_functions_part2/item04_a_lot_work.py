
def my_first_decorator( input_funct  ):
    def wrapper():
        print( "This happend first" )
        input_funct()
        print("This happend at the end")

    return wrapper


def my_second_decorator( input_funct ):
    def wrapper():
        print("#########################")
        input_funct()
        print("--------------------------")

    return wrapper




def say_hello():
    print("Hello")


#just print hello
say_hello()
print()

first_combo = my_first_decorator(  say_hello )
first_combo()

print()

second_combo = my_second_decorator( say_hello )
second_combo()
