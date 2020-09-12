
##
colors = [ "red", "green", "blue", "blue"  "black" ,"red" , "white", "purple", "blue" ]

## Get count items in arrays
red_total = colors.count("red")
blue_total = colors.count("blue")
violet_total = colors.count("violet")
print( f"Red = {red_total}, blue= {blue_total}, violet = { violet_total} \n" )


## join
hyphen_str = "-".join( colors )
blank_str = "".join( colors )
dot_str = ".".join( colors)

print( f"The list join with hyphen {hyphen_str }" )
print( f"The list join with blank {blank_str }" )
print( f"The list join with dot {dot_str }\n" )
