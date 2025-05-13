from django.db import models
from django.utils import timezone

def get_today():
    return timezone.now().date()

class Post(models.Model):
    id=models.AutoField(primary_key=True)
    title= models.CharField(max_length=100)
    body=models.TextField(default="")
    created_at=models.DateField(default=get_today)

    def __str__(self):
        return self.title

class Comment(models.Model):
    id=models.AutoField(primary_key=True)
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment=models.TextField()
    created_at=models.DateField(default=get_today)

    def __str__(self):
        return f'comment on {self.post}'

