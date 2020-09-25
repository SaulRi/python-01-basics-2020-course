
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


def repeat_it( inpu_funct ):
    def wrapper( *args, **kwargs ):
        inpu_funct( *args, **kwargs )
        inpu_funct( *args, **kwargs )
        inpu_funct( *args, **kwargs )
        inpu_funct( *args, **kwargs )

    return wrapper    

def fail_with_args( inpu_funct ):
    def wrapper(  ):
        inpu_funct( )
        inpu_funct( )
        inpu_funct( )

    return wrapper

    
        