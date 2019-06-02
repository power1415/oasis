from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    song = "supersonic!"
    return render(request, 'test.html', {
        'song': song,
        'error_message': "404 messages",
    })