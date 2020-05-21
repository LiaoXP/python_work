import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    # return HttpResponse("hello, django")
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def hello_there(request, name):
    # now = datetime.now()
    # formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # match_object = re.match("[a-zA-Z]+", name)

    # if match_object:
    #     clean_name = match_object.group(0)
    # else:
    #     clean_name = "friend"

    # content = "hello there, " + clean_name + ", it's " + formatted_now

    # return HttpResponse(content)
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )