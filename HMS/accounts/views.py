from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserCreationForm


# In views.py
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()  # This saves the user to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}! You have successfully registered.')
            return redirect('login')  # Redirect to login or another page
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})



