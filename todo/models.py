from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)


class Task(models.Model):
    description = models.CharField(max_length = 200)
    due_date = models.DateField(auto_now = True)
    created_at = models.DateField(auto_now =True)
    category = models.ForeignKey(Category, default = "general", on_delete = models.CASCADE)