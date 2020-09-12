
## Create user class
class User:
    #constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old"


leo = User("Leopoldo", "user@mail.com", 41 )

print( f"type of leo { type(leo) }" )
print( f"users are {leo} " )
print ( f"Name is { leo.name} , email is {leo.email} and age { leo.age}  " )
print( leo.greet() )


