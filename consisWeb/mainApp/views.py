from django.shortcuts import render, redirect
from .forms import SignupForm
from .models import User, Role, Permission

def has_permission(user, permission_name):
    # Check if the user has the required permission
    return user.role.permissions.filter(permission_name=permission_name).exists()

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            designation = form.cleaned_data['designation']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            user = User.objects.create(name=name, designation=designation, role=role)
            user.set_password(password)
            user.save()

            return redirect('signup_success')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

def some_protected_view(request):
    # Assume 'request.user' is the logged-in user
    if has_permission(request.user, 'edit'):
        # Allow the user to edit
        return render(request, 'edit_page.html')
    else:
        # Deny access
        return redirect('access_denied')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)  # Log the user in
                return redirect('home')  # Redirect to the home page after successful login
            else:
                # If the authentication fails, show an error message
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)  # Logs out the user
    return redirect('login') 

from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')
