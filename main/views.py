from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect

from .forms import UserForm, OrderForm
from .models import Order, Client


def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")


def contact(request):
    return render(request, "main/contact.html")


def track_your_order(request):
    tracking_id = request.GET.get("tracking_id")
    order = get_object_or_404(Order, trackingId=tracking_id)
    return render(request, 'main/orderTracking.html', {'order': order})


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
                return redirect('index')
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
        mobileNumber = request.POST['mobile_number']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            client = Client(mobile_no=mobileNumber, user=user)
            client.save()
            login(request, user)
            return redirect('index')
    context = {
        "form": form,
    }
    return render(request, 'main/registration.html', context)


def create_order(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    else:
        form = OrderForm(request.POST or None)
        context = {
            "form": form,
        }
        return render(request, "main/create_order.html",context)
