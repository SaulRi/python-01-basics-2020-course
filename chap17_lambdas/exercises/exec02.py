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
