class Parent():
    def __init__(self,n,a):
        self.__name= n
        self.__age = a

    def get_name( self ):
        return self.__name

    def get_age( self ):
        return self.__age

class child(Parent):
    def __init__(self,n1,a1):
        self.__cname=n1
        self.__cage=a1
        # return Parent.__init__(n1,a1) #old version
        return super ( child , self ).__init__ ( n1,a1 ) #new version

    def get_cname( self ):
        return self.__cname

    def get_cage( self ):
        return self.__cage


if __name__=='__main__':
    c = child('abcd',3)

    age = c.get_age.__name__
    a = age.split('_')

    name = c.get_name.__name__
    n=name.split('_')

    age1 = c.get_cage.__name__
    a1=age1.split('_')

    # name1 = c.__getattribute__('get_cname')
    # print(name1)

    name1=c.get_cname.__name__
    n1=name1.split('_')

    dic={n[1]:c.get_name(), a[1]:c.get_age(), n1[1]:c.get_cname(), a1[1]:c.get_cage()}

    print(dic)

#using __dict__
    dic1={}
    lisdir = c.__dict__

    for x,y in lisdir.items():
        if x.startswith('_child__') :
            var1 = x.split('_child__')
            dic1[var1[1]]=y

        if x.startswith('_Parent__') :
            var1 = x.split('_Parent__')
            dic1[var1[1]]=y

    print(dic1)
