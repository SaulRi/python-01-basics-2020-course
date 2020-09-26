#
selected = input('Type d for collection with data, e for empty or n for null')

#
if selected == 'd':
    collection = []
elif selected == 'e':
    collection = []
else:
    collection = None

#
if collection != None and len(collection) > 0:
    print( f"The first element is { collection[0] }" )
    last_index = len( collection ) -1
    print( f"The last element is { collection[last_index ] } ")
else:
    print("The collection can not be access")

