from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=300, default="Habibi")
    email = models.EmailField()
    about_me = models.TextField()
    image = models.ImageField(upload_to='users/', null=True, blank=True)
    social_github = models.URLField(null=True, blank=True)
    social_linkdin = models.URLField(null=True, blank=True)
    social_twitter = models.URLField(null=True, blank=True)
    social_stackoverflow = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Projects(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message_text = models.TextField()

    def __str__(self):
        return self.email
