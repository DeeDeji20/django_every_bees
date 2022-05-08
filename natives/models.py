from django.db import models

# Create your models here.
class Cohort(models.Model):
    number = models.IntegerField(default=0, unique=True)
    name = models.CharField(max_length= 50, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('Others', 'Others')
)
class Native(models.Model): 
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Others')
    number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


