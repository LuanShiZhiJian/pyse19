from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(blank=True, default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def published(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return 'Post<author=%s,title=%s, text=%s,create_date=%s,published_date=%s>'%\
               (self.author,self.title,self.text,self.created_date,self.published_date)