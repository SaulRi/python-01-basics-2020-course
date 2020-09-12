colors = [  "red", "green", "blue"  ]

if len(colors) > 0:
    print( f"Colors are {colors}" )
    print( f"And length is { len(colors) }" )
else:
    print( "Collection is empty" )

print()

if "green" in colors:
    print("Green is in collection" )   
else:
    print("Color not found")   

print()

if "violet" in colors:
    print("violet exists in collection")    
else:
    print("Color not found") 


## Activity 1
# 1.1 Create a list call new_colors with the values blue, red, violet, white, black
# 1.2 Ask for a color and save in a variable call my_color
# 1.3 Use a if-else structure to evaluate the value of my_color 
# 1.4 If the color exist print the index of the color 
# 1.5 if the color does not exist, print color not found

new_colors = [ 'blue', 'red', 'violet', 'white', 'black' ]
my_color = input('Type your color: ')

if my_color in new_colors:
    index = new_colors.index( my_color )
    print( f"The color {my_color} is in index {index}" )
else:
    print("color not found")    