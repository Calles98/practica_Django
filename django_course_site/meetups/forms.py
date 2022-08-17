from django import forms
# from .models import Participant

# class Registration(forms.ModelForm):
#     class Meta:
#         model = Participant
#         fields = ['email']

class Registration(forms.Form):
    email = forms.EmailField(label = 'Your Email')