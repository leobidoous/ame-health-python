from django.shortcuts import render

# Create your views here.
def gestor(request):
    return render(request, 'gestor/index.html')

def cadastro_gestor_view(request):
    return render(request, 'gestor/cadastro_gestor.html')
