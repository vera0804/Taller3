from django.shortcuts import render, redirect
from .forms import PersonaForm

def registrar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')
    else:
        form = PersonaForm()
    return render(request, 'personas_app/registrar_persona.html', {'form': form})

def exito(request):
    return render(request, 'personas_app/exito.html')
