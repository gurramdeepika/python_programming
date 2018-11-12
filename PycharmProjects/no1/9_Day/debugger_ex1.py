import pdb
def f1(some_arg):
    some_other = some_arg + 1
    print(some_other)
    myadd(some_arg,some_other)
    return f2(some_other)
def f2(some_arg):
    some_other = some_arg + 1
    some_other = 2 * some_other -17
    some_arg = 3 * (some_other + 12)
    myadd(some_arg,some_other)
    some_other = some_other + some_arg
    print(some_other)
    return f3(some_other)
def f3(some_arg):
    some_other = some_arg + 1
    print(some_other)
    return f4(some_other)
def f4(some_arg):
    some_other = some_arg + 1
    some_other = 2 * some_other - 17
    some_arg = 3 * (some_other + 12)
    some_other = myarith( some_other , some_arg )
    print ( some_other )
    return some_other
def myadd(x,y):
    x = 9/x + 1.8*y
    y = 7.8*(x/9 + 2.3/y)
    return x +y
def myarith(x,y):
    x = 9/x + 1.8*y
    y = 7.8*(x/9 + 2.3*y)
    return x + y
pdb.run("f1(1)")

#s - single stepping (executes the code step by step), it will enters in to a function
#p - print
#p some_arg
#n - it will skip the function call and enters the next line
#b - breakpoint (b function name / line number) , if just put b it will give all the breakpoints,
     # here 'c' will go to the next breakpoint
#!variablename -- to change the value in pdb prompt
# disable breakpoint number -- will disable the particular breakpoint
# enable breakpoint number --  will enable the breakpoint which is disabled
# clear breakpoint number -- will delete the breakpoint
#tbreak breakpoint number -- will delete the breakpoint after that breakpoint line exceution
# j line number - will jump in to that line number but should be within the function