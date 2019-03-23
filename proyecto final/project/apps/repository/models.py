from django.db import models

class Repository(models.Model):

    id = models.IntegerField(primary_key=True)

    Name = models.CharField(max_length=150)

    LastCommit = models.DateTimeField()

    LastConsultation = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name