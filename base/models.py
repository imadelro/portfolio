from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    project_image = models.ImageField(upload_to='projects/')
    link = models.URLField()
    tags = models.ManyToManyField(Tag, related_name='projects', blank=True)

    def __str__(self):
        return self.name