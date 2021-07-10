from django.shortcuts import render, redirect
from .forms import UserForm
from .models import MyUser
from django.contrib.auth import authenticate, login

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
    return render (request, 'signup.html', params)


def login(request):
    if request.method == 'POST':
        email_data = request.POST['email_data']
        password_data = request.POST['password_data']
        user = authenticate(request, email=email_data, password=password_data)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('index')
    return render(request,'login.html')


def index(request):
    data = MyUser.objects.all()
    params = {'message':'ユーザー一覧','data':data}
    return render(request, 'index.html', params)


