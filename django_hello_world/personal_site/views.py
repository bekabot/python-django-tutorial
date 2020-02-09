# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1> Hi BekaBot! <h1>")
