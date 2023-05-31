from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from embed_video.fields import EmbedVideoField
from datetime import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.contrib.auth.models import BaseUserManager
from multiselectfield import MultiSelectField



class News(models.Model):
    # CATEGORY_CHOICES = (
    #     ('Adhyatam', 'अध्यात्म'),
    #     ('Khel', 'खेल'),
    #     ('Desh-Videsh', 'देश-विदेश'),
    #     ('Feature', 'फ़ीचर'),
    #     ('MadhyaPradesh', 'मध्यप्रदेश'),
    #     ('Mahanagar', 'महानगर'),
    #     ('MashikPatrika','मासिक पत्रिका'),
    #     ('Vyapar', 'व्यापार'),
    #     ('Cinema','टीवी मूवी'),
    #     ('Video','विडियो')
    # )

  

    title = models.CharField(max_length=255,null=True)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    description = RichTextField()
    tags = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField(default=True,null=True,)
    category = models.CharField(max_length=20,null=True)
    created_at = models.DateTimeField(default=datetime.now(),null=True)
    show_in_home=models.BooleanField(default=False,null=True)
    show_in_headline=models.BooleanField(default=False,null=True)
    def __str__(self):
        return self.title

class Advertisement(models.Model):
   
    title = models.CharField(max_length=255,null=True)
    ctg= models.CharField(max_length=255,null=True,)
    image = models.ImageField(upload_to='advertisements',null=True)
    status = models.BooleanField(default=True,null=True,)
    created_at = models.DateTimeField(default=datetime.now(),null=True)

    def __str__(self):
        return self.title


class AddBanner(models.Model):
    image = models.ImageField(upload_to='banners',null=True)
    status = models.BooleanField(default=True,null=True)
    created_at = models.DateTimeField(default=datetime.now(),null=True)
    def __str__(self):
        return self.image.name


class AddVideo(models.Model):
    title = models.CharField(max_length=255,null=True)
    status = models.BooleanField(default=True,null=True)
    video = EmbedVideoField(null=True)
    created_at = models.DateTimeField(default=datetime.now(),null=True)
    def __str__(self):
        return self.title
    
    # def thumbnail_url(self):
    #     return f'https://img.youtube.com/vi/{self.video_id}/default.jpg'


class AddMashikPatrika(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='PDF_Image/')
    pdf = models.FileField(upload_to='pdfs/')
    status = models.BooleanField(default=True,null=True)

    def __str__(self):
        return self.title
    
class AajKaRashifal(models.Model):
    
    description = RichTextField(null=True)

    # def __str__(self):
    #     return self.description
    


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        if not phone_number:
            raise ValueError("Users must have a phone number")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, phone_number, password, **extra_fields)



class CustomUser(AbstractUser):
    PERMISSION_CHOICES=(
        ('Add News','add news'),
        ('Edit News',"edit news"),
        ('Delete News','delete news')
    )
    phone_number = models.CharField(max_length=15, unique=True)
    status =models.BooleanField(default=True)
    permission=MultiSelectField(choices=PERMISSION_CHOICES, blank=True ,max_choices=3, max_length=30)

    def __str__(self):
        return self.username
