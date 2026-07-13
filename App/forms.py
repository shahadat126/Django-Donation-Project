from django import forms 
from .models import Donation
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['name', 'amount', 'photo']
        
        
class SignupForm(UserCreationForm):
    class Meta:
        model =User
        fields = ['username','email','password1','password2']    
        
