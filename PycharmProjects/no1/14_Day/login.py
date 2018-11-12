f = open('/home/cisco/PycharmProjects/no1/mysite/myapp/uservalid.txt')
ruser = f.readlines()
for rvalue in ruser:
    values = rvalue.strip().split(':')
    print(values[0],values[1])
