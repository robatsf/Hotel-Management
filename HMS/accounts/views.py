from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserCreationForm
from .models import Profile

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)

        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            phone_number=form.cleaned_data.get('phone_number')
            # user.Profile.phone_number=phone_number
            # user.Profile.save()
            messages.success(request,f'welcome {username}!')
            return redirect('login')
    
    else:
        form=UserCreationForm()
    
    return render(request,'accounts/register.html',{'form':form})


def profile(request):
    user_profile = request.user.profile  # Access the profile of the logged-in user
    return render(request, 'accounts/profile.html', {'profile': user_profile})