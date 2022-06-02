# importing url paths from the django folder
from django.urls import path
# importing views derived from the paths
from . import views

# showing the possible routes that will go to a particular view then naming those routes 
urlpatterns = [
    path('', views.home, name="home"),
    path('rate/', views.rate_prof_page, name="rate page"),
]

