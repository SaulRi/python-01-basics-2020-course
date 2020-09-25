

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


@my_first_decorator
def super_whee():
    print("Wheeee!")

@my_second_decorator
def cool():
    print('Cool!')



super_whee()

print()

cool()

@my_first_decorator
@my_second_decorator
def sandwich():
    print("In the middle...")


print()

sandwich()


