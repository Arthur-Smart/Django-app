from django.contrib import admin
from .models import User_Profile , User_Post, Like_Post, Follow,Comment

# Register your models here.
admin.site.register(User_Profile)
admin.site.register(User_Post)
admin.site.register(Like_Post)
admin.site.register(Follow)
admin.site.register(Comment)
