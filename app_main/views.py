from django.shortcuts import render

# Create your views here.


def index_view(request):
    return render(request, 'app_main/index.html')

def search_view(request):
    return render(request, 'app_main/search.html')
