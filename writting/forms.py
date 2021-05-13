from django import forms
from .models import Tisto

# class CreateWrittingForm(forms.Form):
#   jemok = forms.CharField(max_length=200)
#   naeyong = forms.CharField(widget=forms.Textarea)

#   def save(self, *args, **kwargs):
#     super(CreateWrittingForm, self).save(*args,**kwargs)

class CreateWrittingForm(forms.ModelForm):
  class Meta:
    model = Tisto
    fields = ['jemok', 'naeyong']