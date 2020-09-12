import statistics


data = [ 1.3, 2.7, 0.8, 4.1, 4.3, -0.1 ]
avg = statistics.mean( data )

print( f" the data {data} and the average is { avg } " )
print()

## filter the numbers above the average
above_data = list( filter( lambda current: current > avg , data )  )
print( f"The data above avegare is {above_data} " )
print()

## filter the numbers below the average
below_data = list( filter( lambda current: current < avg , data ) )
print( f"The data below avegare is {below_data} " )
print()