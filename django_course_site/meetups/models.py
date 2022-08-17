from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} ({self.address})'


class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Organizer(models.Model):
    name = models.CharField(max_length=200)
    OrgEmail = models.EmailField(unique=True)
    
    def __str__(self):
        return f'{self.name} ({self.OrgEmail})'


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, blank=True, null=True)
    Organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.slug}'