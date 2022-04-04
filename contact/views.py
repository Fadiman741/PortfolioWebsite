from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'message': message,
        }
        print(data)
    return render(request, "htmlcodes/index.html", {})
