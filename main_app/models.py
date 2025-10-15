from django.db import models
from django.urls import reverse # reverse used to look up a url by name
# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("cat-detail", kwargs={"cat_id": self.id})    
    

class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(max_length=1, 
                            choices=MEALS, 
                            default=MEALS[0][0])
    
    # FK (Foreign Key) Relationship on cat
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE) # delete all feedings for this cat if the owner of this meal is delete
 
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

