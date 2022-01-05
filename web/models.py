from django.db import models


class Home(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="home/",blank=True,null=True)

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="project/")

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
