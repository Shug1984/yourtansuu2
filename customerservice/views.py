from django.shortcuts import render, redirect
from account.models import MyUser
from customerservice.models import Inquiry
from customerservice.forms import InquiryForm

def inquiryformview(request):
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.created_by = request.user
            inquiry.save()
            return redirect('inquiry_complete')
    else:
        form = InquiryForm()
        return render(request,'customerservice/inquiry_form.html', {'form':form})

def InquiryCompleteView(request):
    return render(request, 'customerservice/inquiry_complete.html')


# Create your views here.
