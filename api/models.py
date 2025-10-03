from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password 

class User(models.Model):
    username = models.CharField(max_length=150, unique=True, db_column='user') 
    password = models.CharField(max_length=128) 

    def save(self, *args, **kwargs):
        if not self.id or not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$')): 
             self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    class Meta:
        pass 
        
    def __str__(self):
        return self.username


class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True)
    content = models.TextField()
    createdAt = models.DateTimeField(default=timezone.now)
    imageUrls = models.JSONField(default=list) 
    
    slug = models.SlugField(max_length=255, unique=True)
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ['-createdAt']

    def __str__(self):
        return self.title