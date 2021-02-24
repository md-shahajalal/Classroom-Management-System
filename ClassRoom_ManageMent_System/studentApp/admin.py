from django.contrib import admin
from .models import TeachingClass,JoinedClass,UserProfile
# Register your models here.
admin.site.register((TeachingClass,JoinedClass,UserProfile))
 
