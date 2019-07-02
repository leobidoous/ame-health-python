from django.shortcuts import render

# Create your views here.
def gestor(request):
    return render(request, 'gestor/index.html')