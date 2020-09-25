from my_decorators import repeat_it, fail_with_args

@fail_with_args
def sayMyName(name ):
    print( f"your name is {name}")

@repeat_it
def sayMessage(message):
    print( f"{message} !!")

@repeat_it
def take_two( first, second ):
    print( f"{first} {second} " )


@repeat_it
def take_none(  ):
    print("No argument was passed")

try:
    sayMyName("Polo")
except Exception as error:
    print( error  )
    print()


sayMessage( "Cobra Kai" )
print()


take_two( "Miyagi", "Do" )
print()

take_none()
