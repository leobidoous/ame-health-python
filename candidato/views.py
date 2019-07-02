from django.shortcuts import render
from candidato.forms import CandidatoForm


# Create your views here.
def candidato_view(request):
    return render(request, 'candidato/index.html')

def cadastro_candidato_view(request):
    form = CandidatoForm()
    context = {'form': form}

    return render(request, 'candidato/cadastro_candidato.html', context)
