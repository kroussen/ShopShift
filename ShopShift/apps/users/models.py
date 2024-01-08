from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError


class CustomUserManager(BaseUserManager):
    """
    Менеджер пользователей для модели CustomUser.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Создает и сохраняет обычного пользователя с указанным email и паролем.
        """
        if not email:
            raise ValidationError('Email адрес является обязательным')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        if password is not None:
            user.set_password(password)
        else:
            raise ValidationError('Пароль является обязательным')

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Создает и сохраняет суперпользователя с указанным email и паролем.
        """
        if password is None:
            raise ValidationError('Пароль является обязательным для создания суперпользователя')

        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Кастомная модель пользователя, наследующая AbstractBaseUser и PermissionsMixin.
    """
    username = models.CharField(max_length=50, blank=True, verbose_name="Имя пользователя")
    email = models.EmailField(max_length=200, unique=True, verbose_name="Email пользователя")
    image = models.URLField(blank=True, null=True,
                            default="https://ростр.рф/assets/img/no-profile.png",
                            verbose_name='Изображение пользователя')
    is_active = models.BooleanField(default=True, verbose_name="Активный пользователь")
    is_staff = models.BooleanField(default=False, verbose_name="Администратор")

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
