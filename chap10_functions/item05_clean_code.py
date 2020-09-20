
# Prefered more clean and readable code
def get_centimeters( feet=0, inches=0 ):
    """
        This method will get you the number of centimers
        given the number of feet and inches
        :param float feet: The number of feet
        :param float inches: The number of inches
        :return: The convertion in centimeters
    """    
    feet_to_cm = feet * 12 * 2.54
    inches_to_cm  = inches * 2.54
    return feet_to_cm + inches_to_cm

# Its not about impress any one
def cm( f =0, i =0):
    return ( f * 12 * 2.54 ) + ( i * 2.54 )



get_centimeters( feet= 5)
cm( f=5 )

print("Hasta la vista baby..")