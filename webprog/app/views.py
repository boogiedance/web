from django.shortcuts import render

def about_page(request):
    return render(request, 'about.html')

def links_page(request):
    return render(request, 'links.html')