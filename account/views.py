from django.shortcuts import render,redirect,HttpResponse
from .forms import UserResgisterForm,UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def registration(request):
    if request.method == 'POST':
        forms = UserResgisterForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data["username"]
            password = forms.cleaned_data["password"]

            try:
                User.objects.create_user(username=username,password=password)
                return redirect('user-login')
            except:
                errMsg = "User already exiist"
                context = {'forms': forms, 'errMsg':errMsg}
                return render(request, 'register.html', context)

        else:
            context = {'forms': forms}
            return render(request, 'register.html', context)


    forms = UserResgisterForm()

    context = {'forms':forms}
    return render(request,'register.html',context)

def user_login(request):
    if request.method == 'POST':
        forms = UserLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data["username"]
            password = forms.cleaned_data["password"]

            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('home')
            else:
                errMsg = "Username or Password Does't Match"
                context = {'forms': forms, 'errMsg': errMsg}
                return render(request, 'user_login.html', context)


    forms = UserLoginForm()
    context = {'forms': forms}
    return render(request,'user_login.html',context)

def user_logout(request):
    logout(request)
    return redirect('home')
