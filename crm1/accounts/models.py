from django.db import models
from django.contrib.auth.models import *
(
AbstractBaseUser, BaseUserManager
)
class UserManager(BaseUserManager):
    def create_user(self,email, password=None,is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("users must have an email address")
        if not password:
            raise ValueError("users must have a password")
        users_obj=self.model(
            email=self.normalize_email(email)
        )
        users_obj.set_password(password)
        users_obj.staff = is_staff
        users_obj.admin = is_admin
        users_obj.active= is_active
        users_obj.save(using=self._db)

    def create_staffuser(self,email, password=None):
        user = self.create_user(
                email,
                password=password,
                is_staff=True
        )
    def create_superuser(self,email,password=None):
        user = self.create_user(
                email,
                password=password,
                is_staff=True,
                is_admin=True
        )
        return user






class User(AbstractBaseUser):
    email   = models.EmailField(max_length=255, unique=True,default="")
    full_name=models.CharField(max_length=255, blank=True ,null=True)
    active  = models.BooleanField(default=True)
    staff   = models.BooleanField(default=False)
    admin   = models.BooleanField(default=False) #superuser

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email 

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
     

    @property
    def is_staff(self):
        return self.active

    def has_perm(self, perm, obj=None):
       return self.is_admin

    def has_module_perms(self, app_label):
       return self.is_admin

     



class Customer(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=254, unique=True, blank=False)
    password = models.CharField(max_length=50, blank=False)
    is_active = models.BooleanField(default=False, blank=False)



def __str__(self):
    return self.email
