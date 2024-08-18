from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            eu = request.POST['eu']
            password = request.POST["password"]
            username = ''
            
            try:
                print('login with email')
                username = User.objects.get(email=eu).username
            except:
                print('login with username')
                username = eu
                
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, 'Wrong Username or Email or Password.')


        return render(request, 'accounts/login.html')
    else:
        return redirect('/')


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


@csrf_protect
def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST['email']
            username = request.POST["username"]
            password1 = request.POST['password1']
            password2 = request.POST["password2"]
            if password1 == password2:
                u = User(email=email, username=username)
                u.set_password(password1)
                u.save()
                return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, 'Password and its repeated password are not same.')
                
        return render(request, 'accounts/signup.html')
    else:
        return redirect('/')
    

@csrf_protect
def forgetpass_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST['email']
            username = request.POST["username"]
            password1 = request.POST['password1']
            password2 = request.POST["password2"]
            try:
                u = User.objects.get(username=username, email=email)
                if password1 == password2:
                    u.set_password(password1)
                    u.save()
                    return redirect('/')
                else:
                    messages.add_message(request, messages.ERROR, 'Password and its repeated password are not same.')
            except User.DoesNotExist:
                print('User Does Not Exist')

        return render(request, 'accounts/forgetpass.html')
    else:
        return redirect('/')
