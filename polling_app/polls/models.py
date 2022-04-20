from django.db import models

# Create your models here.


class Candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    party = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Event(models.Model):
    event_name = models.CharField(max_length=200)
    deadline = models.DateTimeField()
    candidate = models.ManyToManyField(Candidate, related_name="events")

    def __str__(self):
        return self.event_name
