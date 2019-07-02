from django.shortcuts import render

# Create your views here.
def candidato_view(request):
    return render(request, 'candidato/index.html')