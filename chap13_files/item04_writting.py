# wrinting file, 6 forms to write a file ( but not limited to)
# write in a file with w option, will override the content, BE CAREFUL

oceans = [ "Pacific", "Atlantic", "Indian", "Southern", "Artic" ]

## Creating file oceans01.txt
with open( "oceans01.txt", "w" ) as file1:
    file1.writelines( oceans )

print( "File oceans01.txt was created" )

## Creating file oceans02.txt
with open( "oceans02.txt", "w") as file2:
    [ file2.write(ocean)  for ocean in oceans ]

print( "File oceans02.txt was created" )

## Creating file oceans03.txt
with open( "oceans03.txt", "w") as file3:
    for ocean in oceans:
            file3.write( ocean)
            file3.write( "\n" )

print( "File oceans03.txt was created" )

## Creating file oceans04.txt
with open( "oceans04.txt", "w") as file4:
    for ocean in oceans:
            file4.write( f"{ocean}\n" )

print( "File oceans04.txt was created" )
            
## Creating file oceans05.txt
with open( "oceans05.txt", "w" ) as file5:
    for ocean in oceans:
        print( ocean, file=file5 )

print( "File oceans05.txt was created" )

## creating file oceans06.txt
with open( "oceans06.txt", "w" )as file6:
    [ print(ocean , file=file6) for ocean in oceans ]

print( "File oceans06.txt was created" )


## now append content to file 06
with open( "oceans06.txt", "a" ) as file7:
    print( 23*"=", file=file7 )
    print( "These are the 5 oceans.", file=file7 )

print( "File oceans06.txt was updated" )