from django.db import models
from django.utils import timezone

class Post(models.Model):
##class means we're crating an object model.Post is the name. models.Model tells Django it's a model, so it should be saved in the DB.'
    author = models.ForeignKey('auth.User') ##links to another model
    title = models.CharField(max_length=200) ##limits the number of characters
    text = models.TextField() ##Long text without a limit. For blog posts.
    created_date = models.DateTimeField(
            default=timezone.now) ##Date and time
    published_date = models.DateTimeField(
            blank=True, null=True) ##Date and time
##abover are properties and declarations thereof.

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
# Create your models here.
