from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {
        "title": "Hello, world!",
        "content": "Welcome"
    }
    if request.user.is_authenticated:
        context['premium_content'] = "YEAAAAH"
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title": "About page",
        "content": "Let's know each other"
    }
    return render(request, "home_page.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "content": "Call me",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    if request.method == "POST":
        print(request.POST)
        print(request.POST.get("fullname"))
    return render(request, "contact/view.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)    
    context = {
        "form": form
    }
    print("User logged in ")
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        print(request.user.is_authenticated)
        if user is not None:
            print(request.user.is_authenticated)
            login(request, user)
            #context['form'] = LoginForm()
            return redirect("/")
        else:
            print("Error")
    return render(request, "auth/login.html", context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        new_user = User.objects.create_user(username, password, email)
        print(new_user)
    return render(request, "auth/register.html", context)
    