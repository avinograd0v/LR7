from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from lab7dj.models import *
from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,logout
from django.contrib import auth

# Create your views here.


class RegistrationForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username', 'placeholder': 'Введите логин', }), \
        min_length=5, label='Login:')
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Введите имя', }), \
        max_length=30, label='Name:')
    surname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'surname', 'placeholder': 'Введите фамилию', }), \
        max_length=30, label='Surname:')
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Введите email', })
    )
    password = forms.CharField(min_length=8, label='Password:', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'password', 'placeholder': 'Введите пароль', }))
    password2 = forms.CharField(min_length=8, label='Confirm password:', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'password2', 'placeholder': 'Повторите пароль', }))

    def save(self):
        u = User()
        u.username = self.cleaned_data.get('username')
        u.password = make_password(self.cleaned_data.get('password'))
        u.first_name = self.cleaned_data.get('name')
        u.last_name = self.cleaned_data.get('surname')
        u.email = self.cleaned_data.get('email')
        u.is_staff = False
        u.is_active = True
        u.is_superuser = False
        u.save()

    def clean_password2(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError('Passwords does not match')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            u = User.objects.get(username=username)
            raise forms.ValidationError('This login already uses')
        except User.DoesNotExist:
            return username
##########################################################################

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success/')
        return render(request, 'registration.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def registration_success (request):
    return render(request, 'reg_success.html')



def authorization (request):
    errors=[]
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username:
            errors.append(' Введите логин ')
        elif not password:
            errors.append(' Введите пароль ')
        else:
            user = authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('success/')
            else:
                errors.append('Неправильный логин или пароль')
        return render(request, 'authorization.html', {'errors': errors, 'username': username})
    return render(request, 'authorization.html', {'users': errors})


@login_required(login_url="/authorization/")
def auth_success(request):
    return render(request, 'auth_success.html')



@login_required
def exit(request):
    logout(request)
    return render(request, 'exit.html')
