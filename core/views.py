from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')

def cadastro(request):
    return render(request, 'core/cadastro.html')