from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()
    postimage = models.ImageField(default="https://i.ytimg.com/vi/njczesGlXaQ/maxresdefault.jpg")
    def __str__(self):
        return self.title