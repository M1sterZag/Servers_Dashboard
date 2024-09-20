from django.shortcuts import render, redirect
from .models import Card
from django.contrib.auth.decorators import login_required
from .forms import CardForm

# Create your views here.
def index(request):
    return render(request, "cards/index.html")


@login_required
def servers(request):
    servers = Card.objects.filter(owner=request.user)
    context = {"servers": servers}
    return render(request, "cards/servers.html", context)


@login_required
def new_server(request):
    if request.method != 'POST':
        form = CardForm()
    else:
        form = CardForm(data=request.POST)
        if form.is_valid():
            new_card = form.save(commit=False)
            new_card.owner = request.user
            new_card.save()
            return redirect('cards:servers')
    context = {'form': form}
    return render(request, 'cards/new_server.html', context)