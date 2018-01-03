from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render
from django.views import generic

from .forms import UserForm
from .models import Order, Client


def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request,"main/about.html")

def contact(request):
    return render(request,"main/contact.html")


class OrderDetailView(generic.DetailView):
    model = Order
    template_name = "main/"


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'main/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # albums = Album.objects.filter(user=request.user)
                return render(request, 'main/index.html')
            else:
                return render(request, 'main/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'main/login.html', {'error_message': 'Invalid login'})
    return render(request, 'main/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            client = Client()
            client.user = user
            client.save()
            return render(request, 'main/index.html')
    context = {
        "form": form,
    }
    return render(request, 'main/register.html', context)
