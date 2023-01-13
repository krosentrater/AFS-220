from django.shortcuts import render

def attractions(request):
    return render(request, 'attractions.html', {})
