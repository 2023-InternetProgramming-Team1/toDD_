from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, SignInForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # 회원가입 성공 후 리다이렉트할 URL
    else:
        form = SignUpForm()
    return render(request, 'join/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request, request.POST)
        if form.is_valid():
            user = authenticate(request, studentId=form.cleaned_data['studentId'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')  # 로그인 성공 후 리다이렉트할 URL
    else:
        form = SignInForm()
    return render(request, 'join/signin.html', {'form': form})
