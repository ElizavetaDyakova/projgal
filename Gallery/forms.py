from django import forms
from django.db.models.query import QuerySet
from django import forms
from core.models import Category

class FilterForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    god_grad = forms.IntegerField(label="Год выпуска", required=False)


from django.contrib.auth.forms import AuthenticationForm, UsernameField


class LoginForm(AuthenticationForm):

    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus': True, 'placeholder': 'Username',
        'class': 'form-control'})
    )

    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль', 'class': 'form-control'}),
    )

    error_messages = {
        'invalid_login': "Введен неправильный логин или пароль",
    }