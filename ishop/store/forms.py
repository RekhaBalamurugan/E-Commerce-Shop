from django import forms 
from django.contrib.auth.models import User
           

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Username'}))
    password = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your Password'}))
    email = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Email'}))
    first_name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your First name'}))
    last_name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Last name'}))

    class Meta():
        model = User
        fields = ('username','password','email','first_name','last_name')

    



      

