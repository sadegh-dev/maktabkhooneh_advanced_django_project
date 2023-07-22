from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager 
)

#from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    This class is designed to handle User-class behaviors.
    """
    def create_user(self, email, password, **extra_fields):
        """create normal user record by email and password fields"""
        if not email:
            #raise ValueError(_("the email is required"))
            raise ValueError("the email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        create normal superuser record by email and password fields
        and set access level of superuser
        """

        # set high-level access field to True
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        # check high-level fields
        if extra_fields.get("is_staff") is not True:
            #raise ValueError(_('for superuser, is_staff field must be True'))
            raise ValueError('for superuser, is_staff field must be True')
        if extra_fields.get("is_superuser") is not True:
            #raise ValueError(_('for superuser, is_staff field must be True'))
            raise ValueError('for superuser, is_staff field must be True')
        return self.create_user(email, password, **extra_fields)


"""
* PermissionsMixin : 
    - include permission and access level and groups.
    - class of inheritance AbstractBaseUSer needs this.
    [click on PermissionsMixin and see details.]

* AbstractBaseUser and AbstractUser has password field by default.
"""



class User(AbstractBaseUser, PermissionsMixin):
    """
    about class User :
    - this inheritances from AbstractBaseUser and PermissionsMixin.
    - email field is unique and PrimaryKey for this table.
    """
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    #is_verified = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email




class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(max_length=5000)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} | {self.first_name} {self.last_name}"

