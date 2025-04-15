from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    post_no = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, models.PROTECT, db_column='author')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'post'


class Comment(models.Model):
    comment_no = models.BigAutoField(primary_key=True)
    post = models.ForeignKey(Post, models.PROTECT, db_column='post')
    author = models.ForeignKey(User, models.PROTECT, db_column='author')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'comment'
