from django import forms


class add_blog(forms.Form):
    blog_title = forms.CharField(max_length=50,widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'btitle',
    }))
    blog_content = forms.CharField(max_length=5000,min_length=100,widget=forms.Textarea(attrs={
        'class':'md-textarea form-control',
        'id':'bcontent',
        'rows':'5',
    }))
    blog_image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input',
        'id': 'bimg',
        'aria-describedby': 'bimg',
    }))