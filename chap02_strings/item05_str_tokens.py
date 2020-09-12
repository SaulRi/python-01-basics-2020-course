
str_msg = 'Hello World'
print( str_msg )
print( "Type of  str_msg",  type( str_msg )  )

words = [ 'Hello', 'World'  ]
print( words )
print( f"Type of words {  type(words) }" )
print()

## Split method
splited_msg = str_msg.split(' ')
print( f"splited message is {splited_msg}  and type is { type(splited_msg) } " )
print()

splited_by_l = str_msg.split('l')
print( f"splited by l is {splited_by_l}  and type is { type(splited_by_l) } " )
print()

splited_by_bye = str_msg.split('bye')
print( f"splited by bye is {splited_by_bye}  and type is { type(splited_by_bye) } " )
print()

## Find index method
print( f"Find  ' ' in { str_msg.find(' ') } "  )
print( f"Find  l in { str_msg.find('l') } "  )
print( f"Find  z in { str_msg.find('z') } "  )
print()

## index of
print(  f"Index of ' '  { str_msg.index(' ') }  "  )
print()

## the string is a "list" of characters, you can get the length
print (  f"The number of character of the string are { len( str_msg )  }" )
print()

## get element by index (position)
print (  f"The index 0 gets { str_msg[0]   }" )
print (  f"The index 1 gets { str_msg[1]   }" )  
print()
