from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


# User manager
# -------------------------------------------------------------------------------------------------
class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):
        if not email:
            raise ValueError('У пользователя должен быть адрес электронной почты')
        if not full_name:
            raise ValueError('Имя не должно быть пустым')

        email = self.normalize_email(email)
        user = self.model(email=email.lower(), full_name=full_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(email, full_name, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


# User model
# --------------------------------------------------------------------------------------------------
class User(AbstractBaseUser, PermissionsMixin):
    TYPE_CHOICES = (
        ('NOT_DEFINED', 'Не выбрано'),
        ('STUDENT', 'Студент'),
        ('TEACHER', 'Педагог'),
        ('MANAGER', 'Менеджер'),
    )

    def validate_image(self):
        file_size = self.size
        megabyte_limit = 3.0
        if file_size > megabyte_limit * 1024 * 1024:
            raise ValidationError(_("The maximum file size should be {}MB").format(str(megabyte_limit)))

    email = models.EmailField(verbose_name=_('email'), max_length=64, unique=True)
    full_name = models.CharField(verbose_name='Полная имя', max_length=64)
    user_type = models.CharField(verbose_name='Тип', max_length=64,
                                 choices=TYPE_CHOICES, default=TYPE_CHOICES[0][1])
    image = models.ImageField(
        verbose_name='Изображение', validators=[validate_image], upload_to='accounts/user/image/',
        blank=True, null=True, help_text='Максимальный размер файла составляет 2 МБ')
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', ]

    def __str__(self):
        return self.full_name

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


# Account model
# ----------------------------------------------------------------------------------------
class Account(models.Model):
    GENDER_CHOICES = (
        ('NOT_DEFINED', 'Не выбрано'),
        ('MALE', 'Ер'),
        ('FAMALE', 'Әйел'),
    )

    CITY_CHOICES = (
        ('NOT_DEFINED', 'Не выбрано'),
        ('SHYMKENT', 'Шымкент'),
        ('ALMATY', 'Алматы'),
        ('ASTANA', 'Астана'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    birthday = models.DateField(verbose_name='День рождение', blank=True, null=True)
    gender = models.CharField(verbose_name='Пол', max_length=64, choices=GENDER_CHOICES,
                              default=GENDER_CHOICES[0][1])
    city = models.CharField(verbose_name='Город', max_length=64,
                            choices=CITY_CHOICES, default=CITY_CHOICES[0][1])
    address = models.TextField(verbose_name='Адрес', max_length=255, blank=True, null=True)
    phone = models.CharField(verbose_name='Телефон', max_length=255, null=True, blank=True)
    account_fill = models.BooleanField(verbose_name='Аккаунт заполнено', default=False)

    def __str__(self):
        return f'Профиль: {self.user}'

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'
