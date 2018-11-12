import httplib2

c = httplib2.HTTPSConnectionWithTimeout("www.python.org",443)
c.putrequest("GET",'/3/tutorial/index.html')
c.putheader("someheader",'somevalue')
c.endheaders()

r = c.getresponse()
data = r.read()
print(data)
c.close()