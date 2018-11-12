from django.template import Template, Context

t = Template('Hello,{{name}}')

for name in('a', 'b', 'c'):
    print(t.render(Context({'name': name})))

person = {'name':'pink ranger', 'age':'24'}

t = Template('{{person1.name.upper}} is {{person1.age}} years old.')
c = Context({'person1': person})
print(t.render(c))

#python manage.py shell < path of the python file --> to execute the file

