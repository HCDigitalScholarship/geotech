from django.urls import path
from . import views


urlpatterns = [
path('', views.get_file, name='get_file'),
 path('get_post', views.get_post, name='get_post')

]

 