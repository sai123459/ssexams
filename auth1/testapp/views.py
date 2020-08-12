from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from testapp import forms

# Create your views here.
def home(request):
    return render(request,'testapp/home.html')


def signup_view(request):
    form=forms.signup_form()
    if request.method=='POST':
        form=forms.signup_form(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})



@login_required
def java_view(request):
    return render(request,'testapp/java.html')
@login_required
def python_view(request):
    return render(request,'testapp/python.html')
@login_required
def aptitude_view(request):
    return render(request,'testapp/aptitude.html')

def logout_view(request):
    return render(request,'testapp/logout.html')