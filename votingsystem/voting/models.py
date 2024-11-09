from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    voter_id = models.CharField(max_length=100)

    class Meta:
        unique_together = ('voter_id', 'candidate')

