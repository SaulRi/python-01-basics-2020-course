import math

def get_circle_area( radius):
    """ Get the area of circle with radius """
    return math.pi * math.pow( radius, 2)


radius_list = [ 2,5, 7.1, 0.3, 10 ]
area_list1 = []
print( f"radious_list is { radius_list }" )

for radius in radius_list:
    area = get_circle_area( radius )
    area_list1.append( area )

print( f"area list is { area_list1 }" )

##  usgin map to get area list
## new_list = list( map( function_to_use, original_list )  )
print( f"The type of map is { map( get_circle_area, radius_list )  }" )
print( f"The type of map is { list( map( get_circle_area, radius_list ) )  }" )

area_list2 = list(  map(get_circle_area, radius_list) )
print( f"The result of this map is { area_list2 }" )
