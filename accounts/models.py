from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.conf import settings
# from django.contrib.auth import get_user_model
# User = get_user_model()
class MyUserManager(BaseUserManager):
    def create_user(self, email, user_type,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            user_type = user_type
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,user_type='admin', password=None):
        user = self.create_user(
            email,
            password=password,
            user_type = user_type
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    TYPE = (
        ('customer', 'customer'),
        ('paperboy','paperboy'),
        ('manager','manager'),
        ('accountant','accountant'),
        ('admin','admin'),
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    user_type=models.CharField(default='customer',max_length=20,choices=TYPE)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

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
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Branch(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Adress(models.Model):
    doorno      = models.CharField(max_length=50)
    colony      = models.CharField(max_length=100)
    landmarak   = models.CharField(max_length=100)
    village     = models.CharField(max_length=100)
    mandal      = models.CharField(max_length=100)
    pincode     = models.CharField(max_length=6)

    def __str__(self):
        return self.landmarak + ' ,'+self.colony

class NewsPaper(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.title
class PaymentProfile(models.Model):
    card_no = models.CharField(max_length=14)
    cvv = models.CharField(max_length=3)
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4)
    def __str__(self):
        return self.card_no

class MonthlyBill(models.Model):
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    payment_profile = models.ForeignKey(PaymentProfile,related_name='monthly_bills',on_delete = models.CASCADE)
    def __str__(self):
        return str(self.amount)
