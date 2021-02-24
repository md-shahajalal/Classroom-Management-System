from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator,random_string_generator

# Create your models here.

class TeachingClass(models.Model):
    teaching_class_id=models.AutoField(primary_key=True)
    slug=models.SlugField(blank=True, null=True)
    class_name=models.CharField(max_length=200)
    class_subject=models.CharField(max_length=70)
    class_section=models.CharField(max_length=50)
    class_timestamp=models.DateTimeField(auto_now_add=True)
    class_code=models.CharField(max_length=20,blank=True, null=True)
    class_author=models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering= ('-class_timestamp',)
        

    def __str__(self):
        return self.class_name + "....."


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.class_code=random_string_generator(size=6)

pre_save.connect(pre_save_receiver, sender=TeachingClass)

class JoinedClass(models.Model):
    class_id=models.AutoField(primary_key=True)
    joined_class=models.ForeignKey(TeachingClass,on_delete=models.CASCADE)
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    joining_date=models.DateTimeField(auto_now_add=True)
    class_code=models.CharField(max_length=50)

    class Meta:
        ordering= ('-joining_date',)

    def __str__(self):
        return self.class_code + "....."
#user profile
class UserProfile(models.Model):
    profile_pic=models.ImageField(default='profile/img/default_profile.png',upload_to='profile/img',null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    dept=models.CharField(default="",max_length=100,null=True,blank=True)
    reg=models.CharField(default="",max_length=30,null=True,blank=True)
    session=models.CharField(default="",max_length=30,null=True,blank=True)
    section=models.CharField(default="",max_length=30,null=True,blank=True)
    bio=models.TextField(default="",max_length=500,null=True,blank=True)
    email=models.CharField(max_length=30,null=True,blank=True)
    phone=models.CharField(default="",max_length=30,null=True,blank=True)

    def __str__(self):
        return self.user.username



    
