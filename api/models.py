from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from .validators import validate_file_extension


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, name, cellphone, password=None):
        if not email:
            raise ValueError('must have user email')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            cellphone=cellphone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, cellphone, password):
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            password=password,
            cellphone=cellphone
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    name = models.CharField(
        max_length=20,
        null=False
    )
    cellphone = models.CharField(
        max_length=20
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'cellphone']


class Full(models.Model):
    full_video = models.FileField(validators=[validate_file_extension])
    date = models.DateTimeField()
    size = models.CharField(max_length=20)
    storage_path = models.CharField(max_length=50)
    recording_time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='full')


class Edited(models.Model):
    edited_video = models.FileField(validators=[validate_file_extension])
    abnormal_type = models.CharField(max_length=20)
    edited_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='edited')
    full = models.ForeignKey(Full, on_delete=models.SET_NULL, null=True, related_name='parts')
