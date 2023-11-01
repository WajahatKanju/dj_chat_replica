from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login


def index(request):
    return render(request, 'chat/frontpage.html', )


def signup(request):
    print("METHOD HERE")
    print(request.method)
    if request.method == "POST":
        print("METHOD POST")
        print(request.POST)
        form = SignUpForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            print(user)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()

    return render(request, 'chat/signup.html', {'form': form})
