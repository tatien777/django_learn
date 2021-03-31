from django.db import models
from django.db.models.aggregates import Max
import datetime 
# Create your models here.
## Tao table: Hoc vien 

# first_name, last_nam,age 
class Student(models.Model):
    first_name = models.CharField('first Name',max_length=100)
    last_name = models.CharField('Last Name',max_length=100)
    age = models.IntegerField('Age')
    address = models.TextField("Address",default="")

    class Meta:
        ## db_table la doi table cho model 
        db_table = "Student"
    def __str__(self):
        return (f"{self.first_name}") 
    
    from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name
    class Meta:
        db_table = "Place"


class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name
    class Meta:
        db_table = "Restaurant"

        
class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)
    class Meta:
        db_table = "Waiter"

class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta: 
        ordering = ['title'] # du de khi get thi no se dc order by title 
        db_table = "Publication"

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']
        db_table = "Article"

    def __str__(self):
        return self.headline

class Courses(models.Model):
    c_code = models.CharField('code of course',max_length=20, primary_key=True, default='PY-2011')
    c_name = models.CharField('name code',max_length=50)
    duration = models.IntegerField('duration',default=1) # the period of month
    c_num = models.ManyToManyField(Student)
    begin_date = models.DateField('date start of course',null=False,default=datetime.date.today())
    class Meta:
        db_table = "Courses"
    def __str__(self):
        return '{}-{}'.format(self.name, self.age)