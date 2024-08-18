from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User


@csrf_protect
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST['email']
            username = request.POST["username"]
            password = request.POST["password"]
            
            try:
                print('login with email')
                username = User.objects.get(email=email).username
            except:
                print('login with username')
                
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

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
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
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
            except User.DoesNotExist:
                print('User Does Not Exist')

        return render(request, 'accounts/forgetpass.html')
    else:
        return redirect('/')
