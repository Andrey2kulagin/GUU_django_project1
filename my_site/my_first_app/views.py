from django.shortcuts import render


def index(request):
    return render(request, "my_first_app/index.html")
