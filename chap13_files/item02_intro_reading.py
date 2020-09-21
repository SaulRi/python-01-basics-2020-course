
def print_content( text_content= "", array_content=[] ):
    """
    This prints a text, and then an array 
    And print the results in terminal
    :param str text_content: The text to be printed
    :param list array_content: The list to be printed
    :return: This method is void (return nothing)
    """
    size = len(array_content)

    print( f"Content of text is :{text_content}." )
    print( f"len of lines is { size }" )    
    print( f"Content of lines is :{array_content}. \n" )
    
    if size > 0:
        print("Printing lines")
        print('-----------------------------------')
        for line in array_content:
            print( line )
            print('-----------------------------------')
    else:
        print("### No lines to print")



def read_first( file_name ):
    """
    This function use the metod read first, and then readLines
    And print the results in terminal
    :param str file_name: The file to be open
    :return: This method is void (return nothing)
    """
    file = open( file_name )
    text = file.read()
    lines = file.readlines()    
    file.close()
    print_content( text, lines )    

def lines_first( file_name ):
    """
    This function use the metod readlines first, and then read
    And print the results in terminal
    :param str file_name: The file to be open
    :return: This method is void (return nothing)
    """
    file = open( file_name )
    lines = file.readlines()
    text = file.read()
    file.close()
    print_content(  array_content=lines,  text_content=text )


read_first('bio.txt')
print()

lines_first('bio.txt')

print('\nHasta la vista baby...')