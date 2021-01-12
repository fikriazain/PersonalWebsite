from django.shortcuts import render

def index(request):
    context = {
        'Judul':'Fikri AUfaa Zain',
    }
    return render(request, 'index.html', context)