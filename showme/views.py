import itertools
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
    featured = projects[len(projects)-1]

    def partition(els):
        # make up for 3 
        els = list(els)
        els.extend([None] * (3 - len(els) % 3))
        print(els)
        for i in range(0, len(els), 3):
            yield els[i: i+3] 

    user_name = request.user.username if request.user.is_authenticated else None

    partitioned = partition(projects)
   
    return render(request, 'showme/offerings.html', {
        'all_projects': partitioned,
        'featured': featured,
        'user_name': user_name
        }) 

class IndexView(generic.ListView):
    template_name = 'showme/index.html'
    context_object_name = 'popular_project_list'

    def get_queryset(self):
        return Project.objects.order_by('-start_date')[:3]