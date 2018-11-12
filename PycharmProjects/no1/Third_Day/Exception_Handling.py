# #Try-Catch
# while True:
#       try:
#           x = int(input("Please enter a number:"))
#           break
#       except ValueError:
#           print("Oops!That was no valid number.Try again....")
#
# #Raise
# import sys
# try:
#     f=open("NewWrite3.txt");s=f.readline()
#     i = int(s.strip())
#     f.close()
# except FileNotFoundError:
#     print("file not found")
# except ValueError:
#     print("Not a number")
# except:
#     print("unexcepted error:",sys.exc_info()[0])
#     raise
#
# #zerodivision error
# import sys
# def divide():
#     x = int(input("enter the divisor"))
#     y = int(input("enter the dividend"))
#     return y/x
#
# try:
#     divide()
# except:
#     print(sys.exc_info()[0])

# user defines exception

try:
    raise Exception ( "spam" , "eggs" )
except Exception as inst:
    print ( type ( inst ) )
    print ( inst.args )
    print ( inst )

# else block

import sys

try:
    f = open ( "NewWrite.txt" )
    val = int ( f.read ( ).strip ( ) )
except FileNotFoundError:
    print ( "No such file" )
except ValueError:
    print ( "Not a number" )
except:
    print ( sys.exc_info ( )[ 0 ] )
    raise
else:
    res = 6 + val
    print ( "Res is " , res )
    f.close ( )

# To get the system args

# try in terminal with  python Third_Day/Exception_Handling.py deepika gurram and check the o/p
print ( "First name is " , sys.argv[ 1 ] )
print ( "Last name is " , sys.argv[ 2 ] )
print ( "Script name is " , sys.argv[ 0 ] )

# Try through terminal python Third_Day/Exception_Handling.py Third_Day/NewWrite.txt
for arg in sys.argv[ 1: ]:
    try:
        f = open ( arg , 'r' )
    except IOError:
        print ( "cannot open" , arg )
    else:
        print ( arg , 'has' , len ( f.readlines ( ) ) , 'lines' )
        f.close ( )
