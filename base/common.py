from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        company_or_individual = request.POST['company_or_individual']

        print("company_or_individual : ",company_or_individual)
        if company_or_individual == 'Individual':
            user = User.objects.create_user(username=username, email=email, password=password,is_staff=False)
            user.save()
        elif company_or_individual == 'Company':
            user = User.objects.create_user(username=username, email=email, password=password,is_staff=True)
            user.save()
            

        # login(request, user)
        # return redirect('login')  # Redirect to the user's profile page

    return render(request, 'signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')  # Redirect to the user's profile page
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
