
secret = "abcd1234"

password = input("Type some secret: ")

if password == secret:
    print("Bingo your password match with secret ")
elif password == "abcd":
    print("Your password is abcd")
elif password == "1234":
    print("your password is 1234")
else:
    print("I cant match the words..")    




## Activity 1
# 1.1 Create a list called colors with the values 'blue', 'red', 'violet', 'white', 'black'
# 1.2 Ask in console for an integer between 0 and 4 and saved in a variable call index
# 1.3 With the index, get the color from the list, and save in a variable call selected
# 1.4 Evaluate if the selected is equal to blue print the message "your color is blue"
# 1.5 but if selected value is equal to white then print "your color is white"
# 1.6 any other value print "Any color"

colors = [  'blue', 'red', 'violet', 'white', 'black' ]

index = int( input("Type an integer between 0 and 4: ") )

selected = colors[ index ]

if "blue" == selected:
    print("your color is blue" )
elif "black" == selected:
    print("your color is black")    
else:
    print("Any color")

