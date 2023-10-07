from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


# User manager
# -------------------------------------------------------------------------------------------------
class UserManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, password=None):
        if not username:
            raise ValueError('Имя пользователя не должно быть пустым')
        if not email:
            raise ValueError('У пользователя должен быть адрес электронной почты')
        if not first_name:
            raise ValueError('Имя не должно быть пустым')
        if not last_name:
            raise ValueError('Фамилия не должно быть пустым')

        email = self.normalize_email(email)
        user = self.model(username=username.lower(), first_name=first_name, last_name=last_name, email=email.lower())
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, first_name, last_name, password=None):
        user = self.create_user(username, email, first_name, last_name, password=password)
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

    username = models.CharField(verbose_name=_('username'), max_length=32, unique=True)
    email = models.EmailField(verbose_name=_('email'), max_length=64, unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=64)
    last_name = models.CharField(verbose_name='Фамилия', max_length=64)
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
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', ]

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

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


# Institution model
# -----------------------------------------------------------------------------------------------
class Language(models.Model):
    name = models.CharField(verbose_name='Язык', max_length=64)
    slug = models.SlugField(verbose_name='Ключ языка', max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


class Institution(models.Model):

    INST_TYPE_CHOICES = (
        ('NOT_DEFINED', 'Не выбрано'),
        ('SCHOOL', 'Школа'),
        ('COMMUNITY', 'Сообщество'),
    )

    OWNERSHIP_CHOICE = (
        ('NOT_DEFINED', 'Не выбрано'),
        ('STATE', 'Государственная'),
        ('PRIVATE', 'Частная'),
    )

    # for schools
    SCHOOL_VIEW_CHOICE = (
        ('NOT_DEFINED', 'Не выбрано'),
        ('GENERAL', 'Общеобразовательная'),
        ('LYCEUM', 'Лицей'),
    )

    SLOPE_VIEW_CHOICE = (
        ('NOT_DEFINED', 'Не выбрано'),
        ('TECH', 'Технические'),
        ('HUMAN', 'Гуманитарные'),
    )

    # for community
    DIR_CHOICE = (
        ('NOT_DEFINED', 'Не выбрано'),
        ('IT', 'Информационные технологии'),
        ('GENERAL_EDU', 'Общее образование'),
    )

    image = models.ImageField(verbose_name='Изображение',
                              upload_to='accounts/institution/images/', blank=True, null=True)
    name = models.CharField(verbose_name='Название', max_length=255)
    ln = models.ManyToManyField(Language, verbose_name='Язык обучения', blank=True)
    inst_type = models.CharField(verbose_name='Тип учреждение', max_length=255,
                                 choices=INST_TYPE_CHOICES, default=INST_TYPE_CHOICES[0][1])
    ownership = models.CharField(verbose_name='Форма собственности', max_length=255,
                                 choices=OWNERSHIP_CHOICE, default=OWNERSHIP_CHOICE[0][1])
    # for schools...
    school_view = models.CharField(verbose_name='Вид', max_length=255,
                                   choices=SCHOOL_VIEW_CHOICE, default=SCHOOL_VIEW_CHOICE[0][1])
    slope = models.CharField(verbose_name='Уклон', max_length=255,
                             choices=SLOPE_VIEW_CHOICE, default=SLOPE_VIEW_CHOICE[0][1])
    # for community
    direction = models.CharField(verbose_name='Направление', max_length=255,
                             choices=DIR_CHOICE, default=DIR_CHOICE[0][1])
    date_created = models.DateField(verbose_name='Год основания')
    license_id = models.CharField(verbose_name='Номер лиценизии', unique=True, max_length=255, blank=True, null=True)
    phone = models.CharField(verbose_name='Телефон', max_length=255, blank=True, null=True)
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True, blank=True, null=True)
    website = models.URLField(verbose_name='Веб-сайт', max_length=255, blank=True, null=True)
    address = models.TextField(verbose_name='Адрес', blank=True, null=True)
    owner = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='Ответственное лицо')
    # ...

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учреждение'
        verbose_name_plural = 'Учреждения'


# Class/Group model
# -----------------------------------------------------------------------------------------------
class ClassGroup(models.Model):
    # for school
    LEVEL_CHOICE = (
        ('NOT_DEFINED', 'Не выбрано'),
        ('ONE', 1),
        ('TWO', 2),
        ('THREE', 3),
        ('FOUR', 4),
        ('FIVE', 5),
        ('SIX', 6),
        ('SEVEN', 7),
        ('EIGHT', 8),
        ('NINE', 9),
        ('TEN', 10),
        ('ELEVEN', 11),
    )

    # for community
    FLOW_CHOICE = (
        ('NOT_DEFINED', 'Не выбрано'),
        ('ONE', 1),
        ('TWO', 2),
        ('THREE', 3),
    )

    name = models.CharField(verbose_name='Название', max_length=255)
    class_level = models.CharField(verbose_name='Уровень класса',
                                   choices=LEVEL_CHOICE, default=LEVEL_CHOICE[0][1])
    flow = models.CharField(verbose_name='Поток',
                            choices=FLOW_CHOICE, default=FLOW_CHOICE[0][1])
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, verbose_name='Учереждение')
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='teacher',
                                blank=True, null=True, verbose_name='Руководитель')
    students = models.ManyToManyField(User, blank=True, verbose_name='Ученики')
    subjects = models.ManyToManyField(to='products.Product', blank=True, verbose_name='Программы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Класс/Группа'
        verbose_name_plural = 'Классы/Группы'
