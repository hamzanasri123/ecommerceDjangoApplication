from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .forms import NewUserForm

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            print(user)
            return redirect('myapp/products')  
    else:
        form = NewUserForm()

    context = {'form': form}
    return render(request, "users/register.html", context)

@login_required
def profile(request):
    return render(request,'users/profile.html')

