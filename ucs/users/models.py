from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
# from django.contrib.auth.models import User
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
  # groups = None
  email = models.EmailField(unique=True, blank=False)
  username = models.CharField(max_length=50, unique=True, blank=False, default='')
  linkedin_url = models.URLField(max_length=300, default='', blank=True)
  github_url = models.URLField(max_length=300, default='', blank=True)
  
  is_active = models.BooleanField(default=True)
  
  USERNAME_FIELD='username'
  REQUIRED_FIELDS=['email']
  
  objects = UserManager()
  
  def __str__(self):
    return self.username
