from django import forms
from django.contrib.auth import password_validation
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
    def clean_student_password(self):
        password = self.cleaned_data['student_password']
        try:
            password_validation.validate_password(password)
            return password
        except forms.ValidationError as errors:
            self.add_error('student_password',errors)

    def clean_student_email(self):
        required_domain = '@nirmauni.ac.in'
        email = self.cleaned_data['student_email']
        if required_domain not in email:
            raise forms.ValidationError("Only University E-mail is allowed!")
        return email


class AddProjectForm(forms.Form):
    project_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'id' : 'project-title',
        'style' : 'font-size: 18px !important;',
    }))
    project_Link = forms.URLField(max_length=50, widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'id' : 'project-link',
        'style' : 'font-size: 18px !important;',
    }))
    project_description = forms.CharField(max_length=300, widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'id' : 'project-description',
        'style' : 'font-size: 18px !important;',
        'rows':'5'
    }))

class EditProjectForm(AddProjectForm):
    id = forms.IntegerField()
    field_order = ['id','project_name','project_Link','project_description']