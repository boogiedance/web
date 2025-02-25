from django import forms

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