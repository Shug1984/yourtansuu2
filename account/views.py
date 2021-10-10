from django.shortcuts import render, redirect, resolve_url
from .forms import UserForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import MyUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, UpdateView, FormView, TemplateView
from django.urls import reverse_lazy


def topview(request):
    return render(request, 'top.html')


def signup(request):
    params = {'message':'','form':None}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            params['message'] = '再入力してください'
            params['form'] = form

    else:
        params['form'] = UserCreationForm()
    return render (request, 'account/signup.html', params)


def loginview(request):
    if request.method == 'POST':
        email_data = request.POST['email_data']
        password_data = request.POST['password_data']
        user = authenticate(request, email=email_data, password=password_data)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    
    return render(request,'account/login.html',{'error_message':'ログインできません'})

@login_required
def logoutview(request):
    logout(request)
    return render(request, 'account/logout.html')


@login_required
def userinfoview(request, pk):
    user_id = request.user.pk
    user_information = MyUser.objects.get(pk = user_id)
    context = {'user_information':user_information}
    return render (request, 'account/user_information.html',context)

@login_required
def usercontrolview(request):
    return render (request, 'account/user_control.html')


class UserChangeView(LoginRequiredMixin, FormView):
    template_name = 'account/user_update.html'
    form_class = UserChangeForm
    success_url = reverse_lazy('user_update_complete')

    def get_initial(self):
        pk = self.request.user.pk
        #pk = self.kwargs['hogehoge']
        user = MyUser.objects.get(pk=pk)
        return {
            'last_name':user.last_name, 'first_name':user.first_name, 'last_kana':user.last_kana, 'first_kana':user.first_kana,
            'zip_code':user.zip_code, 'region_name':user.region_name, 'city_name':user.city_name, 'street_name':user.street_name,
            'building_name':user.building_name, 'tel':user.tel, 'gender':user.gender,'date_of_birth':user.date_of_birth,
        }
    
    def form_valid(self, form):
        pk = self.request.user.pk
        user = MyUser.objects.get(pk=pk)
        user.last_name = form.cleaned_data['last_name']
        user.first_name = form.cleaned_data['first_name']
        user.last_kana = form.cleaned_data['last_kana']
        user.first_kana = form.cleaned_data['first_kana']
        user.zip_code = form.cleaned_data['zip_code']
        user.region_name = form.cleaned_data['region_name']
        user.city_name = form.cleaned_data['city_name']
        user.street_name = form.cleaned_data['street_name']
        user.building_name = form.cleaned_data['building_name']
        user.tel = form.cleaned_data['tel']
        user.gender = form.cleaned_data['gender']
        user.date_of_birth = form.cleaned_data['date_of_birth']
        
        user.save()
        return super().form_valid(form)

class PasswordChange(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'account/change_password.html'
    success_url = reverse_lazy('change_password_complete')
   

class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'account/change_password_complete.html'


class PasswordReset(PasswordResetView):
    subject_template_name = 'registration/password_reset_subject.txt'
    email_template_name = 'resgistration/password_reset_email.html'
    template_name = 'account/reset_password.html'
    success_url = reverse_lazy('reset_password_complete')
    
class PasswordResetDone(PasswordResetDoneView):
    template_name = 'account/reset_password_complete.html'

class PasswordResetConfirm(PasswordResetConfirmView):
    success_url = reverse_lazy('reset_password_complete')
    template_name = 'account/reset_password_confirm.html'

class PasswordResetComplete(PasswordResetCompleteView):
    tempalte_name = 'account/reset_password_finish.html'

@login_required
def homeview(request):
    return render(request, 'home.html')

def testview(request):
    return render(request, 'account/testview.html')



