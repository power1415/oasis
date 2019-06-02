from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    song = "Don't look back in anger"
    return render(request, 'test.html', {
        'song':song
    })