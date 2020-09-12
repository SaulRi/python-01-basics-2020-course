number1 = 880.0
number2 = 40
number3 = 10
number4 = 3

print( f"Number1 value is {number1} and type is {type(number1)}" )
print(  "Number2 value is {0} and type is {1}".format( number2, type(number2) )  )

## Basic operations
print ( f"The sum of {number1} and {number2} is { number1 + number2 }"  )
print ( f"The rest of {number1} and {number2} is { number1 - number2 }"  )
print ( f"The mult of {number1} and {number2} is { number1 * number2 }"  )
print ( f"The div of {number1} and {number2} is { number1 / number2 }"  )

## Pow
print ( f"{number3} pow 3 is { number3**3  }"  )

## Div and module
print ( f"The div of {number3} and {number4} is { number3 / number4 }"  )
print ( f"The integer part divi  {number3} and {number4} is { number3 // number4 }"  )
print ( f"The module of divi  {number3} and {number4} is { number3 % number4 }"  )


## Precedence order