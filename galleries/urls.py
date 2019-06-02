from django.urls import path

from . import views

app_name = 'galleries'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:author_id>/gallery/', views.display, name='display'), 
    path('<int:author_id>/gallery/images/machu.jpg', views.display2, name='display2'), 
    
]