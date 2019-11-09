from django.urls import path
from django.contrib.auth import views as auth_views

from .import views

app_name = 'showme'

urlpatterns = [
     path('', views.home_page, name='index'),
     path('offerings', views.offerings, name='offerings'),
     path('login', auth_views.LoginView.as_view(template_name='showme/login.html')),
     path('logout', auth_views.LogoutView.as_view()),
    # path('', views.IndexView.as_view(), name='index')
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),

]