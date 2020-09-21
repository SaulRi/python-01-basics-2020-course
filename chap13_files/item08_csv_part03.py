r"""
item08_csv_part03.py - Sample using for read a csv file and generate a new one with some rueles
"""

import csv
from datetime import datetime


def generate_daily_stock ( tup_data ):
    """
    This function create a csv file with the calculation of daily stocks
    :param tuple tup_data: A tuple with two elements 0 is the header data(list of strings), 
        and index 1 is and array of arrays (data of the source cvs)
    :return: a boolean indicating where the file is created    
    """
    with open( 'daily_stock.csv', 'w' ) as file:
        writer = csv.writer( file )

        # Create the header for the 'new' file
        writer.writerow( [ 'Date', 'Return' ] )

        data = tuple_data[1]
        size = len( data ) -1

        for index in range( size ):
            todays_data = data[index]
            todays_date = todays_data[0]
            todays_price =  todays_data[-1]

            yesterday_data = data[ index + 1 ]
            yesterday_price = yesterday_data[-1]

            daily_return = ( todays_price - yesterday_price ) / yesterday_price
            formated_date =  todays_date.strftime( '%m/%d/%Y' )
            
            #writer.writerow( [ todays_date, daily_return  ] )
            writer.writerow( [ formated_date, daily_return  ] )    

    print( f"number of returned rows are {size}")

    return True


def get_csv_data( csv_path ):
    """
    This function read a csv file ang get the header and the data
    And return a tuple with the header and the get data
    :param str csv_path: The full path where our csv file is placed    
    :return: A tuple with header and data
    """
    with open( csv_path, newline="" ) as csv_file:
        reader = csv.reader( csv_file )
        header = next( reader )

        data = []
        for row in reader:
            # [ Date,Open,High,Low,Close,Volume,Adj Close ]
            date =  datetime.strptime(  row[0] ,  '%m/%d/%Y' )
            open_price = float(  row[1] )
            high = float( row[2] )
            low = float( row[3] )
            close = float( row[4] )
            volume = int( row[5] )
            adj_close = float( row[6]  )
            data.append( [ date, open_price, high, low, close, volume, adj_close ] )

    print( f"{ len(data) } rows were added to data"  )

    return ( header, data )


if __name__ == "__main__":    
    tuple_data = get_csv_data('google_stock_data.csv')

    is_created = generate_daily_stock( tuple_data )





