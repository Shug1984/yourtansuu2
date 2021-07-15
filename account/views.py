from django.shortcuts import render, redirect, resolve_url
from .forms import UserForm, UserCreationForm, UserChangeForm
from .models import MyUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, UpdateView, FormView
from django.urls import reverse_lazy


def signup(request):
    params = {'message':'','form':None}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('original_login')
        else:
            params['message'] = '再入力してください'
            params['form'] = form

    else:
        params['form'] = UserCreationForm()
    return render (request, 'user_registration/signup.html', params)


def loginview(request):
    if request.method == 'POST':
        email_data = request.POST['email_data']
        password_data = request.POST['password_data']
        user = authenticate(request, email=email_data, password=password_data)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('original_login')
    
    return render(request,'user_registration/login.html',{'error_message':'ログインできません'})


def logoutview(request):
    logout(request)
    return render(request, 'user_registration/logout.html')


def homeview(request):
    return render(request, 'home.html')


class UserChangeView(LoginRequiredMixin, FormView):
    template_name = 'user_registration/userupdate.html'
    form_class = UserChangeForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        #formのupdateメソッドにログインユーザーを渡して更新
        form.update(user=self.request.user)
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # 更新前のユーザー情報をkwargsとして渡す
        kwargs.update({
            'email' : self.request.user.email,
            'first_name' : self.request.user.first_name,
            'last_name' : self.request.user.last_name,
        })
        return kwargs



@login_required
def indexview(request):
    return render(request, 'index.html')


