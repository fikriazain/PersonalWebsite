from django.shortcuts import render

def index(request):
    context = {
        'Judul':'Selamat Datang'

    }
    return render(request, 'index.html', context)