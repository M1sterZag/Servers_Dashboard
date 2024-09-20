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


@login_required
def delete_server(request, server_id):
    server = Card.objects.get(id=server_id)
    if server.owner != request.user:
        raise Http404
    if server:
        server.delete()
    return redirect("cards:servers")


@login_required
def edit_server(request, server_id):
    server = Card.objects.get(id=server_id)
    if server.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = CardForm(instance=server)
    else:
        form = CardForm(instance=server, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('cards:servers')
    context = {'card': server, 'form': form}
    return render(request, 'cards/edit_server.html', context)