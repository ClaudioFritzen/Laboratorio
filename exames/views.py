from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TiposExames

@login_required
def solicitar_exames(request):
    tipos_exames = TiposExames.objects.all()
    if request.method == "GET":
        return render(request, 'solicitar_exames.html', {'tipos_exames': tipos_exames})