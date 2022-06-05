from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import EmailValidator

class AccountManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have email")
        if not username:
            raise ValueError("User must have username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        user.save()

        return user
    

    def create_superuser(self, email, username, password, **extra_fields):
        user = self.create_user(
            email=email,
            username = username,
            password = password,
            **extra_fields
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class Account(AbstractBaseUser, PermissionsMixin):

    TIER_CHOICES = (
        ('Basic', 'BASIC'),
        ('Premium', 'PREMIUM'),
        ('Enterprise', 'ENTERPRISE'),
    )

    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(verbose_name='email', max_length=100, unique=True, validators=[EmailValidator(message="Wrong email!")])
    tier = models.CharField(max_length=10, choices=TIER_CHOICES, default='Basic')
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

