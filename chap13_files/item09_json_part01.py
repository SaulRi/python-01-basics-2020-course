"""

"""

## Reading a json data

import json

with open( 'Movies.json', 'r'   ) as json_file:
    data = json.load( json_file )

print( f"movies_data type is {type(data)}" )
print( data )

print( f"Movies are: { data['movies'] } \n" )
print( f"Favorites Movies are: { data['favourites'] } \n" )


## Reading some string like a JSON
str_value = """
[
  {
    "id": 1,
    "isActive": true,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
      "name": "Romaguera-Crona",
      "catchPhrase": "Multi-layered client-server neural-net",
      "bs": "harness real-time e-markets"
    }
  },
  {
    "id": 2,
    "isActive": true,
    "name": "Ervin Howell",
    "username": "Antonette",
    "email": "Shanna@melissa.tv",
    "address": {
      "street": "Victor Plains",
      "suite": "Suite 879",
      "city": "Wisokyburgh",
      "zipcode": "90566-7771",
      "geo": {
        "lat": "-43.9509",
        "lng": "-34.4618"
      }
    },
    "phone": "010-692-6593 x09125",
    "website": "anastasia.net",
    "company": {
      "name": "Deckow-Crist",
      "catchPhrase": "Proactive didactic contingency",
      "bs": "synergize scalable supply-chains"
    }
  },
  {
    "id": 3,
    "isActive": false,
    "name": "Clementine Bauch",
    "username": "Samantha",
    "email": "Nathan@yesenia.net",
    "address": {
      "street": "Douglas Extension",
      "suite": "Suite 847",
      "city": "McKenziehaven",
      "zipcode": "59590-4157",
      "geo": {
        "lat": "-68.6102",
        "lng": "-47.0653"
      }
    },
    "phone": "1-463-123-4447",
    "website": "ramiro.info",
    "company": {
      "name": "Romaguera-Jacobson",
      "catchPhrase": "Face to face bifurcated interface",
      "bs": "e-enable strategic applications"
    }
  }
]
"""


print("\n\nUSER LIST \n")
user_list = json.loads( str_value )
print( user_list )


## from dictionary to json string
## this is usefull when doing fetch or some rest operation

unique_movie = data['favourites'][ 0 ]
print ( f"unique movie data is { unique_movie }\n" )

data_to_str = json.dumps( unique_movie )
print( f"Type is { type(data_to_str) } \n" )

## review the original title field. 
print( f"data to string is  { data_to_str  } " )


## doing again
data_to_str2 = json.dumps( unique_movie,  ensure_ascii=False  )

## review the original title field again. 
print( f"Pringing aing data to string is  { data_to_str2  } " )


## from dictionary to json file
print( f"Our dicctionary unique_movie { unique_movie }" )

with open('uniqui_ascii.json', 'w' ) as ascii_file:
    json.dump( unique_movie, ascii_file )
print( 'unique_ascii.json is created' )


with open ( 'unique_data.json', 'w', encoding="utf-8" ) as unique_file:
    json.dump( unique_movie, unique_file, ensure_ascii=False  )

print('unique json file was created')