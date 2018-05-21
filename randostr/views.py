from django.shortcuts import render
from django.utils.crypto import get_random_string


def index(request):
    context = {
        "unique_id": get_random_string(length=8)
    }
    return render(request, 'index.html', context)

