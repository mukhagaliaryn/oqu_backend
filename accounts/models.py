from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


# User manager
# -------------------------------------------------------------------------------------------------
class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):
        if not email:
            raise ValueError(_('The user must have an email address'))
        if not full_name:
            raise ValueError(_('The full name should not be empty'))

        email = self.normalize_email(email)
        user = self.model(email=email.lower(), full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(email, full_name, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# User model
# ----------------------------------------------------------------------------------------------------------------------
class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('NOT_DEFINED', _('Not selected')),
        ('MALE', _('Male')),
        ('FAMALE', _('Famale')),
    )

    def validate_image(self):
        file_size = self.size
        megabyte_limit = 3.0
        if file_size > megabyte_limit * 1024 * 1024:
            raise ValidationError(_('The maximum file size should be {}MB').format(str(megabyte_limit)))

    email = models.EmailField(verbose_name=_('email'), max_length=64, unique=True)
    full_name = models.CharField(verbose_name=_('Full name'), max_length=64)
    image = models.ImageField(
        verbose_name=_('Image'), validators=[validate_image], upload_to='accounts/user/image/',
        blank=True, null=True, help_text=_('The maximum file size is 2 MB'))
    birthday = models.DateField(verbose_name=_('Birthday'), blank=True, null=True)
    gender = models.CharField(verbose_name=_('Gender'), max_length=64, choices=GENDER_CHOICES,
                              default=GENDER_CHOICES[0][1])

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
        verbose_name = _('User')
        verbose_name_plural = _('Users')


# Account model
# ----------------------------------------------------------------------------------------------------------------------
class Account(models.Model):
    CITY_CHOICES = (
        ('NOT_DEFINED', _('Not selected')),
        ('SHYMKENT', 'Шымкент'),
        ('ALMATY', 'Алматы'),
        ('ASTANA', 'Астана'),
    )

    ACCOUNT_TYPE = (
        ('USER', _('User')),
        ('AUTHOR', _('Author')),
        ('LLP', _('Limited Liability Partnership')),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    account_type = models.CharField(verbose_name=_('Account type'), max_length=64,
                                    choices=ACCOUNT_TYPE, default=ACCOUNT_TYPE[0][1])
    id_number = models.CharField(verbose_name=_('ID number account'), max_length=64, blank=True, null=True, unique=True)
    specialty = models.CharField(verbose_name=_('Specialty'), max_length=64, blank=True, null=True)
    city = models.CharField(verbose_name=_('City'), max_length=64,
                            choices=CITY_CHOICES, default=CITY_CHOICES[0][1])
    address = models.TextField(verbose_name=_('Address'), max_length=255, blank=True, null=True)
    phone = models.CharField(verbose_name=_('Phone'), max_length=255, null=True, blank=True)
    website = models.URLField(verbose_name=_('Website'), max_length=255, null=True, blank=True)
    about = models.TextField(verbose_name=_('About'), max_length=120, blank=True, null=True)

    account_fill = models.BooleanField(verbose_name=_('Is filled out'), default=False)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')
