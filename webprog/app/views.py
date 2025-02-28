from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpRequest
from datetime import datetime

def about_page(request):
    return render(request, 'app/about.html')

def links_page(request):
    return render(request, 'app/links.html')

def log_in_page(request):
    return render(request, 'app/log_in.html')


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

def registration(request):
    """Renders the registration page."""
    assert isinstance(request, HttpRequest)
    if request.method == "POST":  # после отправки формы
        regform = UserCreationForm(request.POST)
        if regform.is_valid():  # валидация полей формы
            reg_f = regform.save(commit=False)  # не сохраняем автоматически данные формы
            reg_f.is_staff = False  # запрещен вход в административный раздел
            reg_f.is_active = True  # активный пользователь
            reg_f.is_superuser = False  # не является суперпользователем
            reg_f.date_joined = datetime.now()  # дата регистрации
            reg_f.last_login = datetime.now()  # дата последней авторизации
            reg_f.save()  # сохраняем изменения после добавления данных
            return redirect('about')  # переадресация на главную страницу после регистрации
    else:
        regform = UserCreationForm()  # создание объекта формы для ввода данных нового пользователя
    return render(
        request,
        'app/registration.html',
        {
            'regform': regform,  # передача формы в шаблон веб-страницы
            'year': datetime.now().year,
        }
    )

def profile(request):
    if not request.user.is_authenticated:
        return redirect('log_in')
    return render(request, 'app/profile.html')