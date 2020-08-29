from django.shortcuts import render
from .models import customer


def home(request):
    context = {
        'customer': customer.objects.all()
    }
    return render(request, 'customer/home.html', context)


def about(request):
    return render(request, 'customer/about.html', {'title': 'about'})
