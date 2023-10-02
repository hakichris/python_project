from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         print("at least i got here")
         if form.is_valid():
              print("yes the form is validated")
              username = form.cleaned_data.get('username')
              messages.success(request, f'Acccount created for {username}!')
              return redirect('blog-home')
    else:
        print("i am here, I did not make it")
        form = UserCreationForm()
       
    return render(request, 'users/register.html', {'form': form})
 
