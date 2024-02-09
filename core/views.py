from django.shortcuts import render

from portafolio.models import Project


# Create your views here.
def index(request):
    return render(request, 'core/index.html')
def about(request):
    return render(request, 'core/about.html')
def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'core/portfolio.html',{"projects": projects})
def contact(request):
    return render(request, 'core/contact.html')