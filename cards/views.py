from django.shortcuts import render
from .models import Card

# Create your views here.
def index(request):
    return render(request, "cards/index.html")


def servers(request):
    servers = Card.objects.all()
    context = {"servers": servers}
    return render(request, "cards/servers.html", context)