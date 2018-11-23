from django.template import Template, Context

t = Template('{{var}} -- {{var.upper}} -- {{var.isdigit}}')

print(t.render(Context({'var':'hello'})))

t = Template('Item 2 is {{items.2}}.')
c = Context({'items':['apples','bananas','carrots']})

print(t.render(c))