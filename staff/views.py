from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,'stafftemplates/home.html')

def loginstaff(request):
    return render (request,'stafftemplates/logins.html')

def staffpage(request):
    return render (request,'stafftemplates/staffpage.html')