from django.db import models

# Create your models here.

class BlogPost(models.Model):
    Title = models.CharField(max_length=100)
    AuthorName = models.CharField(max_length=50)
    Content = models.CharField(max_length=2000)
    PostedDate = models.DateField('Date Published')


class Comment(models.Model):
    Blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    NickName = models.CharField(max_length=50)
    Email = models.EmailField()
    Content = models.CharField(max_length=2000)
    PostedDate = models.DateField()