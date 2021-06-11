from django.db import models

# Create your models here.

class ShowManager(models.Model):
    def validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Show description should be at least 10 characters"
        return errors


class Show(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    releaseDate = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ShowManager()

