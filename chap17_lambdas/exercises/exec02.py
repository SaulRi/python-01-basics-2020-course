from functools import reduce

## From this list
animal_list = [
    { "type" : "monkey", "emoji": "🐒", "name":"Chita" , "diet": "herbivorous" },
    { "type" : "raccoon", "emoji": "🦝", "name": "RJ" , "diet": "omnivore"  },
    { "type" : "fox", "emoji": "🦊" , "name": "Jony" ,  "diet" : "carnivorous" },
    { "type" : "wolf", "emoji": "🐺" , "name": "Jacob" , "diet" : "carnivorous" },
    { "type" : "tiger", "emoji": "🐅" , "name":"Toño"   ,"diet" : "carnivorous" },
    { "type" : "unicorn", "emoji": "🦄",  "name":"Magic", "diet": "herbivorous"  }
]
#print( f"Original list is { animal_list }" )
print()

### get the following object
"""
{
    "herbivorous" : {
        "total" : 2,
        "animals": [ ('🐒',"monkey" ,"Chita"), ('🦄',"unicorn" , "Magic")  ]
    },
    "omnivore" :  {
        "total" : 1,
        "animals": [ ('🦝',"raccoon" ,"RJ") ]
    },
    "carnivorous" : {
        "total" : 3,
        "animals": [ ('🦊',"fox" ,"Jony"), ('🐺',"wolf" ,"Jacob"), ('🐅',"tiger" ,"Toño") ]
    } 
}
"""
def get_animal_tup(animal):
    return ( animal['emoji'], animal['type'], animal['name'] )


def build_zoo( zoo, animal ):
    #print( f"zoo is {zoo}" )
    #print( f"animal is {animal}" )

    diet = animal["diet"] 

    if diet in zoo :
        zoo_element = zoo[diet]
        total = zoo_element['total'] 
        zoo_element['total'] = total + 1
        zoo_element['animals'].append( get_animal_tup(animal) )
    else:
        zoo[diet] = {
            "total" : 1,
            "animals": [ get_animal_tup(animal)  ]
        }

    return zoo    


zoo_resume = reduce(  build_zoo, animal_list, {} )
print( f"the zoo is { zoo_resume }" )