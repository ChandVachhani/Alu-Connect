from django import forms

class LoginForm(forms.Form):
    identifier = forms.CharField(max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control',
                                      'style':'font-size: 18px !important;',
                                      'id':'uname'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'id':'login-password',
        'style':'font-size: 18px !important;',
    }))

class StudentSignUpForm(forms.Form):
    student_first_name = forms.CharField(max_length=25,widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'fname',
        'style': 'font-size: 18px !important;',
    }))
    student_last_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'lname',
        'style': 'font-size: 18px !important;',
    }))
    student_email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'e-mail',
        'style': 'font-size: 18px !important;',
    }))
    student_username = forms.CharField(max_length=25, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'cuname',
        'style': 'font-size: 18px !important;',
    }))
    student_password = forms.CharField(max_length=25, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'signup-password',
        'style': 'font-size: 18px !important;',
    }))