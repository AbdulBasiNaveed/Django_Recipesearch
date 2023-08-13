from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True , blank=True)
    recipe_name =models.CharField(max_length=100)
    recipe_details =models.TextField(max_length=300)
    recipe_image =models.ImageField()
    recipe_count =models.IntegerField(default=1)


    