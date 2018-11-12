#shared memory and message queue are the fastest interprocess communication techniques and
# file is the slowest thing and primitive type of technique

import pdb

def some_div(some_int):
   # pdb.set_trace ( )
    print("Start int",some_int)
    ret_int = 10/some_int
    print("End some int",some_int)
    return ret_int
if __name__ == '__main__':
    try:
        some_div(0)
    except:
        import sys
        tb = sys.exc_info()[2]
        pdb.post_mortem(tb) #execption is passed as a argument , stops and print at the line where exception occured
    # finally:
    #     print(pdb.runeval("some_div(2)"))

#r - runs the current funtion ex:every statment is a function
#c - continue to the next step as well
#q - quit

#pdb.run - will just run the program and will not return any value if the function is having a return statement also
#pdb.runravl - same as run but will return the value if the funtion is having a return statement

#pdb.set_trace() is a function used as a breakpoint and be placed in any line in a function

