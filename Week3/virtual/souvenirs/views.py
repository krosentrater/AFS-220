from django.shortcuts import render

def souvenirs(request):
    return render(request, 'souvenirs.html', {})
