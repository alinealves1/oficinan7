from django.shortcuts import render, redirect
from app.cadastro import ClienteForm
from app.models import Cliente
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    data = {}
    data['db'] = Cliente.objects.all()
    return render(request, 'index.html',data)

def cadastro(request):
    data = {}
    data['cadastro'] = ClienteForm()
    return render(request, 'cadastro.html', data)

def create(request):
    registro = ClienteForm(request.POST or None)
    if registro.is_valid():
        registro.save()
        return redirect('home')


def create(request):
    registro = ClienteForm(request.POST or None)
    if registro.is_valid():
        registro.save()
        return redirect('home')

def view(request, pk):
    data = { }
    data['db'] = Cliente.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = { }
    data['db'] = Cliente.objects.get(pk=pk)
    data['cadastro'] = ClienteForm(instance=data['db'])
    return render(request, 'cadastro.html', data)

def update(request, pk):
    data = { }
    data['db'] = Cliente.objects.get(pk=pk)
    registro = ClienteForm(request.POST or None, instance=data['db'])
    if registro.is_valid():
        registro.save()
        return redirect('home')

def delete(request, pk):
    db = Cliente.objects.get(pk=pk)
    db.delete()
    return redirect('home')

def consulta(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Cliente.objects.filter(Nome__icontains=search)
    else:
        data['db'] = Cliente.objects.all()
    #all = Cliente.objects.all()
    #paginator = Paginator(all, 2)
    #pages = request.GET.get('page')
    #data['db'] = paginator.get_page(pages)
    return render(request, 'consulta.html', data)