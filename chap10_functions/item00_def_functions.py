
'''
1) Use the reserved word def
2) Assign a name to your function
3) Use parenthesis (), that indicates python is a callable element
4) End with :
5) Define the "body" of the function
'''
def do_nothing():
    ''' This function do nothing..., it can be disappointing :(  '''
    pass

# print without the (), just to see the definition of this function.
print ( do_nothing  )


# Invoke the function
do_nothing()

# Invoke again the function
do_nothing()

# Invoke one last time the function
do_nothing()

print("### Print the dir of the function  ")
print( dir(do_nothing) )

# Print the documentation of the function
help( do_nothing )


print( "Hasta la vista baby..." )