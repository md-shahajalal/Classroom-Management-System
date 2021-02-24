from django.contrib import admin
from .models import Notice,Faculty,Course,Class,ClassRoom

# Register your models here.
admin.site.register(Notice)
admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(ClassRoom)
admin.site.register(Class)