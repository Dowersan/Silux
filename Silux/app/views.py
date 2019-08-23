from django.shortcuts import render
from django.views.generic import ListView
from app.models import *


# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    model = Post


def index_view(request):
    return render(request, 'index.html', {})
