from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime
from cloudinary.models import CloudinaryField

# Create your models here.
class User_Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    service = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    biography = models.TextField(blank=True)
    profilePic = CloudinaryField('image', default='default.jpg')
    created_At = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class User_Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100, blank=True)
    service = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    cost = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    image = CloudinaryField('image', default='default.jpg')
    profileImg = CloudinaryField('image', default='default.jpg')
    created_At = models.DateTimeField(default=datetime.now)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user


class Like_Post(models.Model):
    post_id = models.CharField(max_length=300)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Follow(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user

class Comment(models.Model):
    comment = models.CharField(max_length=500)
    post_id = models.CharField(max_length=500, blank=True, null=True)
    post_related = models.ForeignKey(User_Post, on_delete=models.CASCADE, blank=True, null=True)
    commenter = models.CharField(max_length=100)
    created_At = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.commenter

