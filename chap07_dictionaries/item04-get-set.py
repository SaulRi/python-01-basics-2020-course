book = {}

"""
    "tile" : "Thinking in Python",
    "year" : 2019,
    "pages": 1500
"""

book["title"] = "Thinking in Python"
book["year"] = 2019
book["pages"] = 1500
book["foo"] = 'dummy'

print( f"Book is {book}\n" )

del book["foo"]

print( f"After delete foo, Book is {book}" )
