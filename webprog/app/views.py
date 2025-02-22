from django.shortcuts import render

def about_page(request):
    return render(request, 'app/about.html')

def links_page(request):
    return render(request, 'app/links.html')