
## 
animal_list = [
    { "type" : "monkey", "emoji": "🐒"  },
    { "type" : "raccoon", "emoji": "🦝"  },
    { "type" : "fox", "emoji": "🦊"  },
    { "type" : "wolf", "emoji": "🐺"  },
    { "type" : "tiger", "emoji": "🐅"  },
    { "type" : "unicorn", "emoji": "🦄"  }
]
print( f"Original list is {animal_list}" )

emoji_list = list( map(  lambda animal: animal["emoji"]  , animal_list )  )
print( f'Result is {emoji_list}')