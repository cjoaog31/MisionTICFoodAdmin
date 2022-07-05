from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from os import environ
import random

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password
        """
        user = self.create_user(username=username, password=password)
        user.admin = True
        user.staff = True
        user.save(using=self.db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Username', max_length = 15, unique=True)
    name = models.CharField('Name', max_length = 30)
    email = models.EmailField('Email', max_length = 100)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    USERNAME_FIELD = 'username'
    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.name

    def get_short_name(self):
        # The user is identified by their email address
        return self.name

    def __str__(self):
        return '{}: {}'.format(self.username, self.name)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin