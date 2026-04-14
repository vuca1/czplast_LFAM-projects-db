from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control"
    }))

    subject = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control"
    }))

    body = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control"
    }))
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={
        "class": "form-control"
    }))