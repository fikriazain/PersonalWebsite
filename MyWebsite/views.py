from django.shortcuts import render

def index(request):
    context = {
        'Judul':'Selamat Datang'
        'headline':'LOL'
    }
    return render(request, 'index.html', context)