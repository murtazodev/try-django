from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('default')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def login_view_old(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Invalid username or password"}
            return render(request, 'accounts/login.html', context)
        login(request, user)
        return redirect('default')
        # validate(username, password)
    return render(request, 'accounts/login.html', {})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('logged-out')
    return render(request, 'accounts/logout.html')

def logged_out_view(request):
    return render(request, 'logged_out_users.html')

def register_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user_form = form.save()
        return redirect('login-view')
    return render(request, 'accounts/register.html', { 'form': form })
