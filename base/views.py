from django.shortcuts import render
from.models import Project

# Create your views here.

def portfolio(request):
    projects = Project.objects.all()
    template_name = 'portfolio.html'
    return render(request, template_name, {'projects':projects})


