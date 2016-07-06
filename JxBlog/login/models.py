from django.db import models
from django.contrib import admin
# Create your models here.

class BlogUser(models.Model):
	username=models.CharField(max_length=50);
	userpwd=models.CharField(max_length=50);

class UserAdmin(admin.ModelAdmin):
	list_display = ('username','userpwd')

admin.site.register(BlogUser,UserAdmin)