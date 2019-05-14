from django.contrib.auth import authenticate
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,
                    "home.html",
                    {
                    },
                )


def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

    return render(request,
                    "login.html",
                    {
                    },
                )

def register(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        branch_name = request.POST['branch_name']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']


    return render(request,
                    "register.html",
                    {
                    },
                )

def logout(request):
    return render(request,
                    "login.html",
                    {
                    },
                )