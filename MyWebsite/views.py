from django.shortcuts import render

def index(request):
    context = {
        'Judul':'Fikri Aufaa Zain',
    }
    return render(request, 'index.html', context)