
def go_to_fight( first="Miguel", last="Diaz" ):
    """ 
    This method tell you who win the final tournament
    :param str first: The first name of the fighter, by default value is Miguel
    :param str last: The last name of the fighter, by default value is Diaz
    :return: The string message announcing who win the tournament
    """
    return f"{first} won the All Valley Tournament"

#go_to_fight(  )
#go_to_fight( last="Larusso", first="Amanda" )    


help( go_to_fight )