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