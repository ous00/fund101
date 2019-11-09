from django.http import HttpResponse
from django.shortcuts import get_object_or_404,  render
from django.urls import reverse
from django.views import generic

from .models import Project

def home_page(request):
    projects = Project.objects.order_by('-start_date')[:3]
    user_name = request.user.username if request.user.is_authenticated else None
    return render(request, 'showme/index.html', {
        'popular_project_list': projects,
        'user_name': user_name
        })

def offerings(request):
    projects = Project.objects.order_by('-start_date')
    featured = projects[0]

    def partition(els):
        for i in range(0, len(els), 3):
            yield els[i: i+3] 

    user_name = request.user.username if request.user.is_authenticated else None
    return render(request, 'showme/offerings.html', {
        'all_projects': partition(projects),
        'featured': featured,
        'user_name': user_name
        }) 

class IndexView(generic.ListView):
    template_name = 'showme/index.html'
    context_object_name = 'popular_project_list'

    def get_queryset(self):
        return Project.objects.order_by('-start_date')[:3]