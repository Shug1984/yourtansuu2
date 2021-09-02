from django import forms
from customerservice.models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['title','content','requested_response']
        widget = {
            'requested_response':forms.RadioSelect
        }
    


