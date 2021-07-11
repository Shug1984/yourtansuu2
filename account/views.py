from django.shortcuts import render, redirect
from .forms import UserForm
from .models import MyUser
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def signup(request):
    params = {'message':'','form':None}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            params['message'] = '再入力してください'
            params['form'] = form

    else:
        params['form'] = UserForm()
    return render (request, 'index.html', params)


def loginview(request):
    if request.method == 'POST':
        email_data = request.POST['email_data']
        password_data = request.POST['password_data']
        user = authenticate(request, email=email_data, password=password_data)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('signup')
    
    return render(request,'login.html')

@login_required
def homeview(request):
    return render(request, 'index.html')


