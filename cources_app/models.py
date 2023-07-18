from django.db import models


class courceManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['name']) < 2:
            errors["name"] = "book title should be at least 5 characters"
        if len(postData['description']) < 4:
            errors["description"] = "book description should be at least 10 characters"
        return errors

class cource(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = courceManager()
