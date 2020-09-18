class User:
    #constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old"



class Student(User):

    def __init__( self, name, email, age, student_id ):
        super().__init__( name, email, age )
        self.student_id = student_id

    def print_student_data(self):
        print( f"My Name is {self.name} and my id is {self.student_id} " )    



s1 = Student( "Leopoldo", "leopoldo@gmail.com", 41,  "001" )

print( s1.greet()  )

s1.print_student_data()