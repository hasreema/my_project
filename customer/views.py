from django.shortcuts import render

customer = [
    {
        'name': 'Reema Hassouna',
        'id': '123456789',
        'Email': 'reema@gmail.com',
        'payment': 'xxx'
    },
    {
        'name': 'Mansour Hassouna',
        'id': '123456788',
        'Email': 'mansour@gmail.com',
        'payment': 'xxx'
    }
]


def home(request):
    context = {
        'customer': customer
    }
    return render(request, 'customer/home.html', context)


def about(request):
    return render(request, 'customer/about.html', {'title': 'about'})
