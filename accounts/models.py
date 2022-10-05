from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser, PermissionsMixin
from django.core.validators import MaxLengthValidator
from accounts.managers import CustomUserManager
from django.utils import timezone
import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField
# Create your models here.ff
from django.db.models import Q

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(('email adress'),unique=True)
    # phone_no = models.IntegerField(('phone'),unique=True,default="Null")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(default=timezone.now)
    is_specialuser = models.BooleanField(default=True)
    is_educator = models.BooleanField(default=False)
    is_businessEducator = models.BooleanField(default=False)
    
    
    """
    
    Modifying primary field from username to email to primary verification
    
    """
    
    fields=[email]
    USERNAME_FIELD = 'email'
    EMAIL_FIELD=['email']
    phone_regex = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    phone = models.CharField(max_length=255, validators=[phone_regex], blank = True, null=True)
    REQUIRED_FIELDS=[]
    objects = CustomUserManager()
    
    class Types(models.TextChoices):
        TEACHER = "Teacher", "TEACHER"
        STUDENT = "Student", "STUDENT"
        
    default_type = Types.STUDENT
    type = MultiSelectField(choices=Types.choices, default=[], null=True, blank=True)
    
    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.id:
            self.type.append(self.default_type)
        return super().save(*args, **kwargs)

Exams = (
    ('10th board cbse','1OTH BOARD CBSE'),
    ('11th board cbse','11TH BOARD CBSE'),
    ('12th board cbse','12TH BOARD CBSE'),
    ('8th board cbse','8TH BOARD CBSE'),
    ('9th board cbse','9TH BOARD CBSE'),
    ('iit jee', 'IIT JEE'),
    ('iit jee advance', 'IIT JEE ADVANCED'),
    ('Neet', 'NEET'),
    ('Upsc', 'UPSC'),
    ('Sat','SAT'),
    ('Ielts','IELTS'),
)

class student_details(models.Model):
    user            = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    profile         = models.ImageField(default=" ",upload_to='')
    first_name      = models.CharField(default=" ",max_length=20)
    last_name       = models.CharField(default=" ",max_length=20)
    pincode         = models.CharField(default=" ",max_length=15)
    age             = models.CharField(default=" ",max_length=2)
    intrested_exam  = models.CharField(max_length=20,choices=Exams, default='10th board cbse')
    
    

class TeacherManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        #return super().get_queryset(*args, **kwargs).filter(type = CustomUser.Types.SELLER)
        return super().get_queryset(*args, **kwargs).filter(Q(type__contains = CustomUser.Types.STUDENT))

class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        #return super().get_queryset(*args, **kwargs).filter(type = CustomUser.Types.CUSTOMER)
        return super().get_queryset(*args, **kwargs).filter(Q(type__contains = CustomUser.Types.TEACHER))



class Student(CustomUser):
    default_type= CustomUser.Types.STUDENT
    class Meta:
        proxy = True
    def read():
        print("Student can read question papers")
    @property
    def showAditional(self):
        return self.student

class Teacher(CustomUser):
    default_type= CustomUser.Types.TEACHER
    object = TeacherManager()
    class Meta:
        proxy = True
    
    def publish():
        print("Teacher can publish question paper")
    @property
    def showAditional(self):
        return self.teacher