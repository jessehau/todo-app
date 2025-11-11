from django.db import models
from django.contrib.auth.models import User

#luokka kategorioille
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
#luokka prioriteetille
class Priority(models.Model):
    level = models.CharField(max_length=50)

    def __str__(self):
        return self.level

#luokka tehtävälle
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
