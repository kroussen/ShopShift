from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    # Форма регистрации, наследуемая от UserCreationForm
    email = forms.EmailField(label='Email пользователя')

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']

    def clean(self):
        # Переопределение метода clean для дополнительной валидации
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")

        return cleaned_data


class LoginForm(AuthenticationForm):
    # Форма входа, наследуемая от AuthenticationForm
    email = forms.EmailField(label='Email пользователя')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

    class Meta:
        model = CustomUser
        fields = ['email', 'password']

    def __init__(self, request=None, *args, **kwargs):
        # Переопределение конструктора для удаления поля 'username'
        super().__init__(request, *args, **kwargs)
        del self.fields['username']

    def clean(self):
        # Переопределение метода clean для дополнительной валидации
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            # Попытка аутентификации пользователя
            user = authenticate(request=self.request, email=email, password=password)
            if user is None:
                raise forms.ValidationError("Пользователь не найден. Проверьте правильность введенных данных.")

        return cleaned_data


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'image']

    def clean_email(self):
        email = self.cleaned_data['email']
        user_with_same_email = CustomUser.objects.exclude(id=self.instance.id).filter(email=email)
        if user_with_same_email.exists():
            raise forms.ValidationError("Пользователь с таким Email уже существует")
        return email
