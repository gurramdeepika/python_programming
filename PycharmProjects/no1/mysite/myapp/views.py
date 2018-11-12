from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
import datetime as dt
from django.template import Context, Template
from myapp.models import *

def say_hello(request,name):
    if name == 'san':
        return HttpResponse("hello",name)
    else:
        return HttpResponse('hi',name)

def current_datetime(request,firstvar):
    now = dt.datetime.now()
    html = "<html><body>it is now \
           %s.</body></html>" %now
    # return HttpResponse(html,firstvar)
    return HttpResponse(html)

#to pass the offset in the url
def hours_ahead(request,offset):
    offset = int(offset)
    dt1 = dt.datetime.now() + dt.timedelta(hours=offset)
    html = "<html><body>In %s hour(s),it will be %s.</body></html>"%(offset,dt1)
    return HttpResponse(html)

def template_context(request):

    t=Template('Hello,{{name}}')

    for name in ('a','b','c'):
        print(t.render(Context({'name': name})))


from django.shortcuts import render_to_response

def current_datehtml(request):
    now  = dt.datetime.now()
    return \
    render_to_response('current_datetime.html',{'current_date':now})


def create_form(request):
    # return render_to_response("sample.html",{})
    return render(request,'sample.html')


def search(request):
    if 'name' in request.POST:
        # message = 'you searched for: %r' % request.GET['name']
        name = request.POST['name']
        lis = Publisher.objects.filter (name = name)

    return render_to_response('searched_values.html',{'values':lis})

from django.forms import ModelForm

class ArticleForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title','authors','publisher','publication_date']

def register(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
    return render_to_response('form.html',{'article':article_form})


def searchcolor(request):
    if 'favcolor' in request.GET:
         message = 'you searched for: %r' % request.GET['favcolor']
    else:
        message = 'you have searched for invalid value'
    return HttpResponse(message)

def getcolor(request):
    return render_to_response('cookie.html',{})

def set_color(request):
    if 'favcolor' in request.GET:
        response = HttpResponse("your favorite color is now %s" % request.GET['favcolor'])
        response.set_cookie('favcolor',request.GET["favcolor"])
        return response
    else:
        return HttpResponse("you didn't give a favorite color")

def show_color(request):
    if 'favcolor' in request.COOKIES:
        return HttpResponse("your favcolor is %s" %request.COOKIES['favcolor'])
    else:
        return HttpResponse("you don't have a favorite color")

def login(request):
    if request.method == 'GET':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            return HttpResponse("your logged in")
    return HttpResponse ( "your not logged in" )

def login_user(request):
    return render_to_response ( 'login.html' , {} )

def login_set_cookie(request):
    if request.method == 'GET':
        if request.GET['user'] and  request.GET['pass']:
            user  = request.GET[ 'user' ]
            password = request.GET['pass']
            f = open('/home/cisco/PycharmProjects/no1/mysite/myapp/uservalid.txt')
            ruser = f.readlines()
            print(ruser)
            count = 0
            for rvalue in ruser:
                values = rvalue.strip().split(':')
                if user == values[0] and password == values[1]:
                    response=HttpResponse ( "Successfully Logged In ")
                    response.set_cookie ( 'username' , request.GET[ "user" ] )
                    response.set_cookie ( 'password' , request.GET[ "pass" ] )
                    count =+1
                    return response

            if count == 0:
                return HttpResponse ( "No Registered User Found" )
        else:
            return HttpResponse("Invalid login user")

def show_user(request):
    if 'username' in request.COOKIES and 'password' in request.COOKIES:
        return HttpResponse(" UserName: %s , Password: %s" %(request.COOKIES['username'],request.COOKIES['password']))
    else:
        return HttpResponse("No user found")

def logout_user(request):
    if 'username' in request.COOKIES and 'password' in request.COOKIES:
        response=HttpResponse (render(request,"logout.html") )
        response.delete_cookie('username')
        response.delete_cookie('password')
        return response
    else:
        return HttpResponse("Logout Falied")

def search_user(request):
    if 'username' in request.COOKIES and 'password' in request.COOKIES:
        return render(request,'Searchlogin.html')

