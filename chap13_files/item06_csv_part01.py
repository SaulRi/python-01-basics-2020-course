
csv_path = 'google_stock_data_mini.csv'
lines = [ line for line in open( csv_path ) ]
number_lines = len( lines )

print("Data is")
for current in lines:
    print( current )
print()
print( f"\nNumber of lines are {number_lines}" )

raw_header = lines[0]
first_line = lines[1]

print( f"Raw Header is:{raw_header}." )
print( f"First line is:{first_line}." )


print( f"Raw Header (Trim) is:{raw_header.strip()  }." )
print( f"First line (Trim) is:{first_line.strip()  }." )

print( f"Array of header is:{raw_header.strip().split(',')}" )
print( f"Array of First line is:{first_line.strip().split(',')  }" )

data_set = [ line.strip().split(",")  for line in open( csv_path )  ]
print( f"Dataset: Header is:{ data_set[0] }." )
print( f"Dataset: First line is:{ data_set[1] }." )

# mmm.. now the problem all data is now strings, we lost numeric data


