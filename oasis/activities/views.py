from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, oasis! I'm activities.")