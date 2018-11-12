class MyExcept ( Exception ):
    def __init__ ( self ):
        return

    def __str__ ( self ):
        print ( "My Except Occured" )


def myfunc ( ):
    raise MyExcept


try:
    myfunc ( )
except:
    print ( "Caught An Exception" )
    raise
finally:
    print ( "printed" )
