#stdin
import os
fname = input("enter you first name\n")
lname = input("enter your last name\n")
print("your first name is",fname,'\n')
print("your last name is",lname)


#python3 unix_ex3.py < names.txt
#'<' -- duplicate file discriptor for stdin(KEYBOARD)
files = os.system("ls")
print(files)

