from django import forms

class Formname(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    address=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
    phone=forms.IntegerField()


class NewForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()

class EmiForm(forms.Form):
        loan_amount=forms.IntegerField()
        tenure=forms.IntegerField()
        interest=forms.IntegerField()

class Signup(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())
    address=forms.CharField(widget=forms.Textarea)

class Signin(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
