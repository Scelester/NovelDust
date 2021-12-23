from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login(request):
    if request.method=="POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request, f"you are now logged in as {username}.")
                return redirect("noveldust:index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    contains = {'loginform':form}
    return render(request, 'registration/login.html',context=contains)

def signup(request):
    if request.method == "POST":
        form = NewUserForm()
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, "Signup Sucessfull")
            return redirect("noveldust:index")
        messages.error(request, "Signup unsucessfull, invalid information.")
    form = NewUserForm()
    contains = {"signupform":form}
    return render(request, 'registration/signup.html',context=contains)
