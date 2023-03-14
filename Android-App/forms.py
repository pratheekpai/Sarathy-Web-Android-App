from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField
from django.forms import ModelForm, TextInput, EmailInput, DateInput, PasswordInput, ImageField
from django.forms import widgets
from django.forms.widgets import DateInput, NumberInput
from first_app.models import truck_driver, seller_details, truck_details, job_details

class truckDriver_user_passForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username', 'password', 'email')
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Username'
                }),
            'password': PasswordInput(attrs={
                'class': "form-control",
                'placeholder': 'Password'
                }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'Email'
                }),
        }

class newTruckDriverForm(forms.ModelForm):
    class Meta:
        model = truck_driver
        fields = ['fname', 'mname', 'lname', 'date', 'address', 'phone', 'aadhar_no', 'sex']
        widgets = {
            'fname': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'First Name'
                }),
            'mname': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Middle Name'
                }),
            'lname': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Last Name'
                }),
            'date': DateInput(attrs={
                'class': "form-control",
                'type': 'date',
                'placeholder': 'DOB'
                }),
            'aadhar_no': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Aadhar Number'
                }),
            'sex': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Sex'
                }),
            'address': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Address'
                }),
            'phone': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Phone'
                }),
        }

class newTruckDetailsForm(forms.ModelForm):
    class Meta:
        model = truck_details
        fields = '__all__'
        widgets = {
            'aadhar_no': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Aadhar Number'
                }),
            'license_no': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'License Number'
            }),
            'insurance_no': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Truck Insurance Number'
            }),
            'rc_no': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Registration Certificate Number'
            }),
            'truck_capacity': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Enter your Trucks Capacity(in Tons): '
            }),
            'permit': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'All India(AI) or Not All India(NAI): '
            }),
        }

class seller_user_passForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username', 'password', 'email')
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Username'
                }),
            'password': PasswordInput(attrs={
                'class': "form-control",
                'placeholder': 'Password'
                }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'Email'
                }),
        }

class newSellerDetailForm(forms.ModelForm):
    class Meta:
        model = seller_details
        exclude = ['user', ]
        widgets = {
            'comp_name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Company Name'
                }),
            'comp_address': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Company Address'
                }),
            'phone': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Phone'
                }),
            'trade_license_no': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Trade-License Number'
                })
        }

class newSellerJobForm(forms.ModelForm):
    class Meta:
        model = job_details
        fields = ('trade_license_no', 'source', 'destination', 'goods', 'goods_capacity', 'loading_date', 'unloading_date')
        widgets = {
            'trade_license_no': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Trade License Number'
                }),
            'source': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Source'
                }),
            'destination': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Destination'
                }),
            'goods': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Goods(comma separated)'
                }),
            'goods_capacity': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'How many tons of Goods?'
                }),
            'loading_date': DateInput(attrs={
                'class': "form-control",
                'type': 'date',
                'placeholder': 'Loading Date'
                }),
            'unloading_date': DateInput(attrs={
                'class': "form-control",
                'type': 'date',
                'placeholder': 'Unloading Date',
                })
        }
