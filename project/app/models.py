from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
# create a new attribute in your model


class FormModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    blog_title = models.CharField(max_length=200)
    blog_entry = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.username
