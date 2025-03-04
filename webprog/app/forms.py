from django import forms
from .models import Comment, Blog
from django.contrib import admin
from django.contrib.auth.models import User

class FeedbackForm(forms.Form):
    name = forms.CharField(label="Ваше имя", max_length=100, required=True)
    email = forms.EmailField(label="Ваш email", required=True)
    age = forms.IntegerField(label="Ваш возраст", min_value=1, max_value=120, required=True)
    satisfaction = forms.ChoiceField(
        label="Насколько вам понравился наш сайт?",
        choices=[
            (5, "Отлично"),
            (4, "Хорошо"),
            (3, "Удовлетворительно"),
            (2, "Плохо"),
            (1, "Ужасно")
        ],
        widget=forms.RadioSelect,
        required=True
    )
    improvements = forms.MultipleChoiceField(
        label="Что бы вы хотели улучшить?",
        choices=[
            ("Дизайн", "Дизайн"),
            ("Удобство использования", "Удобство использования"),
            ("Контент", "Контент"),
            ("Производительность", "Производительность")
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    comments = forms.CharField(
        label="Ваши пожелания",
        widget=forms.Textarea,
        required=False
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # Используем модель Comment
        fields = ('text',)  # В форме заполняем только текст комментария
        labels = {'text': "Комментарий"}  # Название поля в интерфейсе

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'short_content', 'content', 'image', 'author']  # Добавлено поле автора
        labels = {
            'title': "Заголовок",
            'short_content': "Краткое содержание",
            'content': "Полное содержание",
            'image': "Изображение",
            'author': "Автор статьи",  # Добавлено название поля в интерфейсе
        }
