from django.shortcuts import render, redirect
from .forms import FeedbackForm

def about_page(request):
    return render(request, 'app/about.html')

def links_page(request):
    return render(request, 'app/links.html')

def pool(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Сохраняем данные в переменные
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            satisfaction = form.cleaned_data['satisfaction']
            improvements = form.cleaned_data['improvements']
            comments = form.cleaned_data['comments']

            # Передаём данные на страницу благодарности
            return render(request, 'app/thank_you.html', {
                'name': name,
                'email': email,
                'age': age,
                'satisfaction': satisfaction,
                'improvements': improvements,
                'comments': comments
            })
    else:
        form = FeedbackForm()
    return render(request, 'app/pool.html', {'form': form})