from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    user_id = models.CharField(max_length=255, primary_key=True)
    user_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    target_weight = models.IntegerField(null=True, blank=True)
    current_bmi = models.FloatField(null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    cardio = models.IntegerField(default=0)
    weightloss = models.IntegerField(default=0)
    weightgain = models.IntegerField(default=0)
    yoga = models.IntegerField(default=0)
    abs = models.IntegerField(default=0)
    upper = models.IntegerField(default=0)
    lower = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    address = models.CharField(max_length=150)
    age = models.IntegerField(null=True, blank=True)
    sex = models.CharField(max_length=1)

    class Meta:
        db_table = 'users'
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.user_name

    def set_password(self, raw_password):
        self.password_hash = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password_hash)



class Receipt(models.Model):
    receipt_id = models.IntegerField(primary_key=True)
    receipt_code = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.CharField(max_length=225)
    date_of_receipt = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'receipts'

class ReceiptItem(models.Model):
    receipt_id = models.IntegerField()
    product_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'receipt_items'