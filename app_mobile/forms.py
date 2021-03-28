from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import Mobile,Order

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username","email", "password1", "password2"]


class OrderCreateForm(ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'name', 'address', 'phone', 'model_name',  'price']
        widgets = {
            'user': forms.TextInput(attrs={'class':'form-control','readonly': 'readonly'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.Textarea(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'model_name': forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),


        }




class OrderSubmitForm(ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'name', 'address', 'phone', 'model_name',  'price', 'status']

        choices = (('pendind', 'pending'),('order dispatched', 'order dispatched'))
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'name': forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),
            'address': forms.Textarea(attrs={'class': 'form-control','readonly': 'readonly'}),
            'phone': forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),
            'model_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),

            'status': forms.Select(choices=choices, attrs={'class': 'form-control'}),
        }

class CreatMobileForm(ModelForm):
    class Meta:
        model = Mobile
        fields = '__all__'
        widgets = {
            'brand_name': forms.TextInput(attrs={'class': 'form-control', }),
            'model_name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'specifications': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'image_1': forms.FileInput(attrs={'class': 'form-control'}),
            'image_2': forms.FileInput(attrs={'class': 'form-control'}),
            'image_3': forms.FileInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),

        }


class FilterForm(forms.Form):
    choices = (('10000', '10000'), ('15000', '15000'), ('20000', '20000'), ('25000', '25000'), ('30000', '30000'), ('35000', '35000'), ('40000', '40000'), ('45000', '45000'), ('50000', '50000'))
    filter = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)

class Search(forms.Form):
    search = forms.CharField()
