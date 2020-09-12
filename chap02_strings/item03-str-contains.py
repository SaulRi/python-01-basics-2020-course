

hello_str = 'Hello World'
print( hello_str )
print()

## count the occurrences
l_total = hello_str.count('l')
orl_total = hello_str.count('orl')
bye_total = hello_str.count('bye')
print( f"The toal of l are { l_total } and total of orl { orl_total } " )
print( f"Total of bye {bye_total}" )
print()


## starts with
print( f"Start with hola ? { hello_str.startswith('hola') } " )
print( f"Start with hello ? { hello_str.startswith('hello') } " )
print( f"Start with Hello ? { hello_str.startswith('Hello') } " )
print()

## ends with
print( f"Ends with mundo ? { hello_str.endswith('mundo') } " )
print( f"Ends with WORLD ? { hello_str.endswith('WORLD') } " )
print( f"Ends with World ? { hello_str.endswith('World') } " )

