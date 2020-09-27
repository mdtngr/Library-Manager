from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, email, phone, roll_no, first_name, password=None):
        if not email:
            raise ValueError("Email??????")
        if not phone:
            raise ValueError("Phone??????")
        # if not fname:
        #     raise ValueError("Name??????")
        # if not year_of_joining:
        #     raise ValueError("YOJ??????")
        if not roll_no:
            raise ValueError("Roll_no??????")

        user    =   self.model(email = self.normalize_email(email), phone = phone, roll_no = roll_no, first_name = first_name)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, phone, roll_no, first_name, password):
        user    =   self.create_user(email = self.normalize_email(email), phone = phone, roll_no = roll_no, first_name =first_name, password = password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)



class UserData(AbstractBaseUser):
    first_name                  =   models.CharField(max_length=10)
    last_name                   =   models.CharField(max_length=10)
    username                    =   models.CharField(max_length=10, default= "new_user")

    email                       =   models.EmailField(verbose_name="email", max_length= 60, unique=True)
    roll_no                     =   models.CharField(max_length=10)
    year_of_joining             =   models.IntegerField(default= 2020, null=True)

    is_admin                    =   models.BooleanField(verbose_name="admin status", default=False)
    is_staff                    =   models.BooleanField(verbose_name="staff status", default=False)
    is_superuser                =   models.BooleanField(verbose_name="superuser status", default=False)
    
    last_login                  =   models.DateField(verbose_name="last login", auto_now=True)
    phone                       =   models.CharField(max_length=10)

    USERNAME_FIELD              = 'email'
    REQUIRED_FIELDS             = ['phone', 'roll_no', 'first_name']
    objects                     = MyAccountManager()

    # def __str__(self):
        # return self.first_name+" | "+self.email + " | "+ self.phone
        # return self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta():
        verbose_name        = "User Detail Row"
        verbose_name_plural = "User Data"


class Userprofile(models.Model):

    user = models.ForeignKey(UserData,on_delete=models.CASCADE,null=True,blank=True)    
    username = models.CharField(max_length=100,blank=True)
    phone_number = models.BigIntegerField(blank=True,null=True)
    email = models.EmailField(max_length=100,blank=True,null=True)
    address = models.TextField(max_length=400,blank=True,null=True)
    profile_picture = models.ImageField(upload_to='static_cdn/profile_image', blank=True,null=True)

    def __str__(self):
        return self.username    

    