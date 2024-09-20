from django.shortcuts import render
from .models import Card
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "cards/index.html")


@login_required
def servers(request):
    servers = Card.objects.filter(owner=request.user)
    context = {"servers": servers}
    return render(request, "cards/servers.html", context)