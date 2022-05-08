from django.db import models

from natives.models import Native

# Create your models here.

class Project(models.Model):
    native = models.ForeignKey(Native, on_delete= models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.TextField(default="https://thumbs.dreamstime.com/b/projects-lead-us-to-success-our-personal-professional-life-necessary-reach-our-goals-everyday-92274762.jpg")

    def __str__(self) -> str:
        return self.title
