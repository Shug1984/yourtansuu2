from django import forms
from django.views.generic.edit import CreateView 

from .models import Closet

class ClosetForm(forms.ModelForm):
   

    class Meta:
        model = Closet
        fields = ('data_id','item_type','season','occasion','item_name','item_color','item_brand','purchase_date','pricing','purchase_place','memo','favorite_level','item_importance')

"""
class ClosetNewCreation(CreateView):
    template_name = 'contents/closet_create.html'
    form_class = ClosetForm

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super(ClosetNewCreation, self).form_valid(form)
"""
    