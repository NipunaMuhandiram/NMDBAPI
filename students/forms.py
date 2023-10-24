from django import forms
from .models import StudentInfo

class CreateStudent(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = "__all__"
      
        widgets = {
            'middlename': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'middlename '}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'birthday Date'}),
            'nic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' NIC'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'student_img': forms.FileInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}),
            'town': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'town'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'mobileno1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'mobileNo 1'}),
            'mobileno2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'mobileNo 2'}),
        }

