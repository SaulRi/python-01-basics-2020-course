## Read Data from CSV file

import csv
from datetime import datetime

csv_path = 'google_stock_data_mini.csv'
csv_file =  open( csv_path, newline="" )
reader = csv.reader( csv_file )

# the first line is the header
header = next( reader )

# iterate the rows to get the data
raw_data =  [ row for row in reader  ]

print( f"Header is:{header}. \n" )

for row  in raw_data:
    print( row )

print()

## but all data is string, we need to format data
data = []
for row in raw_data:
    # [ Date,Open,High,Low,Close,Volume,Adj Close ]
    date =  datetime.strptime(  row[0] ,  '%m/%d/%Y' )
    open_price = float(  row[1] )
    high = float( row[2] )
    low = float( row[3] )
    close = float( row[4] )
    volume = int( row[5] )
    adj_close = float( row[6]  )

    data.append( [ date, open_price, high, low, close, volume, adj_close ] )


for row in data:
    print( row )

print()

for index in range( len( data )  ):
    print(  f"Index = {index} and data is: { data[index] }"  )

print()


print("Full data is")
print(  data  )



