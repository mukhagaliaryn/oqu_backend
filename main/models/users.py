from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.utils.translation import gettext_lazy as _


# CloneUser manager
# -------------------------------------------------------------------------------------------------
class CloneUserManager(BaseUserManager):
    def create_user(self, username, email, full_name, password=None):
        if not username:
            raise ValueError(_('The user must have an email address'))
        if not email:
            raise ValueError(_('The user must have an email address'))
        if not full_name:
            raise ValueError(_('The full name should not be empty'))

        email = self.normalize_email(email)
        user = self.model(username=username, email=email.lower(), full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, full_name, password=None):
        user = self.create_user(username, email, full_name, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# CloneUser model
# ----------------------------------------------------------------------------------------------------------------------
class CloneUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), max_length=128, unique=True)
    username = models.CharField(_('username'), max_length=128, unique=True)
    full_name = models.CharField(_('Full name'), max_length=64)
    image = models.ImageField(_('Image'), upload_to='accounts/user/image/',  blank=True, null=True)
    birthday = models.DateField(_('Birthday'), blank=True, null=True)
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
    groups = models.ManyToManyField(Group, related_name='clone_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='clone_user_set', blank=True)

    objects = CloneUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name', ]

    def __str__(self):
        return self.full_name

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name

    class Meta:
        verbose_name = _('Clone User')
        verbose_name_plural = _('Clone Users')
