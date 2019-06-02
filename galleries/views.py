from django.views import generic
from .models import Galleries
from django.shortcuts import render

class IndexView(generic.ListView):
    template_name = 'galleries/index.html'
    context_object_name = 'galleries_list'
    
    def get_queryset(self):
        return Galleries.objects.all()

    
def display(request, author_id):
    return render(request, 'galleries/ronit/index.html') 

    
def display2(request, author_id):
    return render(request, 'galleries/ronit/images/machu.jpg') 
