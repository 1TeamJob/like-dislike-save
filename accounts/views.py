from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm, SignupForm, UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password=password)
            login(request, user)
            return redirect('/accounts/profile')
    
    
    else:
        form = SignupForm
    
    context = {'form': form}
    return render(request, 'registration/signup.html', context)


def profile(request):
    profile = Profile.objects.get(user=request.user)
    
    context = {'profile': profile}
    return render(request, 'accounts/profile.html', context)



def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            user_profile = profile_form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect(reverse('accounts:profile'))
    
    
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    
    context = {'profile_form': profile_form, 'user_form': user_form}
    return render(request, 'accounts/edit_profile.html', context)




