#oops -- Class
#self becomes the current class object used to access the memebers and variables in  a class
# to make the variables private write the variable as __variable name(2u)
import doctest
class MyClass:
    pass

def myfunc(obj):
    '''

    >>> myfunc(MyClass()) #doctest: +ELLIPSIS
    <__main__.MyClass object at 0x...>
    '''
    return obj

if __name__ == '__main__':
    doctest.testmod(verbose=True)