from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm

def user_login(request):
    if request.method =='POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request,'you Login successfully', 'success')
                return redirect('first:index')
            else:
                messages.error(request,'username or password is not correct!','warning')
    else:
        form = UserLoginForm()
    return render (request,'account/login.html',{'form':form})


@login_required(login_url='account:login')
def user_logout(request):
    logout (request)
    messages.success(request, 'you log-out', 'success')
    return redirect('first:index')
