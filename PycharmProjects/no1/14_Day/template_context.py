
from django.template import Template, Context

t = Template('Hello,{{name}}')

for name in('a','b','c'):
    print(t.render(Context({'name':name})))


    #done in mysite folder