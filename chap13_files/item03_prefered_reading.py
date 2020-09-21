text = ""

## Step 1: Use with to handle the content of a file
with open ("bio.txt") as fileObj:
    text = fileObj.read()

print("The content of bio.txt is ")
print(  text )

## Step 2: Improve , using a "try/catch" to handle posible errors

try:
    print("\n Try to open an imaginary file :P ")
    with open("An_imaginary_file.txt") as fileObj:
        text = fileObj.read()        
except FileNotFoundError as error:
    print( f"Error is {error}" )
    text = None

print( f"The content of imaginary file is {text}" )   
