from django.template import Template, Context

class Person(object):
    def __init__(self,firstname,lastname):
        self.firstname ,self.lastname = firstname, lastname

t = Template("Hello,{{person.firstname}}{{person.lastname}}.")
c = Context({'person': Person('Deepika','Gurram')})
print(t.render(c))