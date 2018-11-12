from django.template import Template,Context

t = Template("My name is {{person.first_name}}.")

# class Person:
#     def first_name( self ):
#         raise AssertionError

# p = Person()
# print(t.render(Context({"person":p})))


class SilentAssertionError(AssertionError):
    silent_variable_failure = True

class Person1():
    def first_name( self ):
        raise SilentAssertionError

p = Person1()
print(t.render(Context({'person':p})))
