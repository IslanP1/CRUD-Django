from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from crud.models import Cliente

# Create your views here.

class ClienteLists(ListView):
    model = Cliente
    queryset = Cliente.objects.all()
    
class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('crud:list')
    
class ClienteUpdate(UpdateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('crud:list')
    
class ClienteDetail(DetailView):
    queryset = Cliente.objects.all()

class ClienteDelete(DeleteView):
    queryset = Cliente.objects.all()
    success_url = reverse_lazy('crud:list')
    
    
    
    
    
