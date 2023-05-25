from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from . import forms


# Create your views here.
def register(request):
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # if form is valid give a message
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username}, Account created successfully, please continue to login")
            return redirect('user-login')
    else:
        # if not a POST request, return an empty form
        form = forms.UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')
