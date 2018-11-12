#use of a format in adapter pattern

class computer:
    def __init__(self,n):
        self.name = n
    def __str__(self):
        return 'the {} computer'.format(self.name)
    def execute( self ):
        return 'executes a program'
# c = computer("mycomp")
# print(c , c.execute())

class synthesizer:
    def __init__(self,n):
        self.name = n
    def __str__(self):
        return 'the {} synthesizer'.format(self.name)
    def play( self ):
        return 'can play a song'
# c1 = synthesizer("mysyn")
# print(c1 , c1.play())

class human:
    def __init__(self,n):
        self.name = n
    def __str__(self):
        return ' {} '.format(self.name)
    def speak( self ):
        return 'can speak'
# c2 = human("mysyn")
# print(c2 , c2.speak())

class Adapter:
    def __init__(self,obj,adapter_methods):
        self.obj = obj
        self.__dict__.update(adapter_methods)
    def __str__(self):
        return str(self.obj)

objects = [computer('Asus')]

# synth = synthesizer('mog')
objects.append(Adapter(synthesizer('mog'),dict(execute=synthesizer('mog').play)))

# human = human('bob')
objects.append(Adapter(human('bob'),dict(execute=human('bob').speak)))

for i in objects:
    print('{}{}'.format(i,i.execute()))


#second example as a first

#use of a format in adapter pattern

class usb:
    def __init__(self,n):
        self.name = n
    def __str__(self):
        return 'the {} usb'.format(self.name)
    def copy( self ):
        return 'copies a program'
# c = computer("mycomp")
# print(c , c.execute())

class projector:
    def __init__(self,n):
        self.name = n
    def __str__(self):
        return 'the {} projector'.format(self.name)
    def play( self ):
        return 'can play a video'
# c1 = synthesizer("mysyn")
# print(c1 , c1.play())

class laptop:
    def __init__(self,n):
        self.name = n
    def __str__(self):
        return ' {} laptop'.format(self.name)
    def connect( self ):
        return 'can connect'
# c2 = human("mysyn")
# print(c2 , c2.speak())

class Adapter:
    def __init__(self,obj,adapter_methods):
        self.obj = obj
        self.__dict__.update(adapter_methods)
    def __str__(self):
        return str(self.obj)

objects = [projector('nice')]

# synth = synthesizer('mog')
objects.append(Adapter(usb('24gb'),dict(play=usb('24gb').copy)))

# human = human('bob')
objects.append(Adapter(laptop('Asus'),dict(play=laptop('Asus').connect)))

for i in objects:
    print(i)
    print('{} {}'.format(i,i.play()))

