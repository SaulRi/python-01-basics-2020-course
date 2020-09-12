## Input data and Casting Data

# use the function input
# Syntax  input ( prompt ), where prompt is a string to show in console

print ('Type your data for registration')
name = input('Please, type your name: ')
age = input('Please, type your age: ')
print("Your name is ", name , "and your age is ", age )
print("The type of name is ", type(name) , "and the type of age is ", type(age) )


## First execute the program with integer values
## The execute again with different type of values (float, string, boolean)
number1 = int( input( 'Please type your first integer number: ' )  )
number2 = int( input( 'Please type your second integer number: ' )  )
print("The type of number1 is ", type(number1) , "and the type of number2 is ", type(number2) )


## Cast with float values
price = float( input("Please, type the cost of your dinner: ")  )
tip = float( input("Please, type the tip for the dinner: ") )
print("The type of price is ", type(price) , "and the type of tip is ", type(tip) )


input('\nType enter to continue... \n')

## Cast to string
number_value1 = 456.6
number_value2 = 345

cast_value1 = str(number_value1)
cast_value2 = str(number_value2)
print("The type of cast_value1 is ", type(cast_value1) , "and the type of cast_value2 is ", type(cast_value2) )
