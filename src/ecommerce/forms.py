from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class": "form-control", 
                "placeholder":"Your full name", 
                "id": "form_full_name"
            }
        )
    )
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Your e-mail"
            }
        )
    )
    content = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                "class": "form-control", 
                "placeholder":"Your message"
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be @gmail.com")
        return email

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget = forms.PasswordInput
    )

class RegisterForm(forms.Form):
    username = forms.CharField(
        label = "usuário"
    )
    email = forms.EmailField(
        label = "e-mail"
    )
    password = forms.CharField(
        label = "senha",
        widget = forms.PasswordInput
    )
    confirm_password = forms.CharField(
        label = "Confirme a senha",
        widget = forms.PasswordInput
    )
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Esse nome de usuário já está sendo usado.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Esse e-mail já está registrado.")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("As senhas devem ser iguais.")
        return data

