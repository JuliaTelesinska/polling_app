from django.db import models

# Create your models here.

class PoliticalParty(models.Model):
    party_name = models.CharField(max_length=50)
    founding_date = models.DateField()
    num_members = models.IntegerField()

    def __str__(self):
        return self.party_name

class Candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    party = models.ForeignKey(PoliticalParty, on_delete=models.CASCADE)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Event(models.Model):
    event_name = models.CharField(max_length=200)
    date = models.DateField()
    candidate = models.ManyToManyField(Candidate, related_name="events")

    def __str__(self):
        return self.event_name
