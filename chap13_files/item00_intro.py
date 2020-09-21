
file_path = './files/myFirstFile.txt'


#Open a file
my_file = open( file_path, 'w' )

# get info of the file
print( f"Name : {my_file.name}" )
print( f"Is Closed : {my_file.close}" )
print( f"Opening mode : {my_file.mode}" )

# Write in file
my_file.write( "Python is Cool!" )
my_file.write( ", but its cooler JavaScript! :)" )
my_file.close()


# Append in the file
my_file = open( file_path, 'a' )
my_file.write("... and I also like Java")
my_file.close()

# read the content
my_file = open( file_path, 'r' )
text_content = my_file.readline()
print( f"The content of my file is: {text_content}" )
my_file.close()
