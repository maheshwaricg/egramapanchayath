from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,'usertemplates/home.html')

def loginuser(request):
    return render (request,'usertemplates/loginu.html')

def userservice(request):
    return render (request,'usertemplates/serviceu.html')

def income(request):
    return render (request,'usertemplates/income.html')

def caste(request):
    return render (request,'usertemplates/caste.html')

def community(request):
    return render (request,'usertemplates/community.html')

def domicile(request):
    return render (request,'usertemplates/domicile.html')

def minority(request):
    return render (request,'usertemplates/minority.html')

def nativity(request):
    return render (request,'usertemplates/nativity.html')

def nonremarriage(request):
    return render (request,'usertemplates/nonremarriage.html')

def ownership(request):
    return render (request,'usertemplates/ownership.html')

def possession(request):
    return render (request,'usertemplates/possession.html')

def userprofile(request):
    return render (request,'usertemplates/userprofile.html')

def about(request):
    return render (request,'usertemplates/about.html')

def feedback(request):
    return render (request,'usertemplates/feedback.html')

def masterpage(request):
    return render (request,'epanchayathtemplates/master.html')
