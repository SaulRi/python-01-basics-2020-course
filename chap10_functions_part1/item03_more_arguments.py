## No arguments function
def ping():
    """This funcition just return... ping! :) """
    return "Doing... ping!"

# two times, the return value, is not store..
ping()
ping()

# "Doing ...ping! now is store in a variable"
ping_variable = ping()


def one_argument( name ):
    return f"Hello! My name is {name}"

one_argument("Leo")
one_argument("Sebastian")

# if no argument is set, send error in script
#one_argument()

def default_argument( name ="Johny" ):
    return f"Hello {name}"


default_argument()
default_argument("Leo")
default_argument("Hugo")
# send error, if more arguments are set
#default_argument( "Jules", "Verne" )

def two_arguments( first, last="Doe" ):
    return f" Hello, {first} {last}"

two_arguments("Jonny")
two_arguments("Juan", "Charrasqueado")

# if only one argument is optional, it must be the last ones
# def wrong_assigment( first="Jonny", last ):
#    return f"Bye bye {first} {last}"

def two_default( first="Jonny", last ="Lawrence" ):
    return f"{first} {last} is watching Cobra Kai!"

two_default()
two_default("Robbie")
two_default( "Larusso", "Daniel" )
two_default( last="Larusso", first="Daniel San" )

print("Hasta la vista baby")