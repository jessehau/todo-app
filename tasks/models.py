from django.db import models

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

#luokka itse tehtävälle
class Task(models.Model):
    title = models.CharField(max_length=200) #tehtävän nimi/otsikko
    complete = models.BooleanField(default=False) #onko tehtävä valmis vai ei
    created = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
