from django.db import models

# Create your models here.

class HistoricalWeather(models.Model):
    city = models.CharField(max_length=100)
    date = models.DateField()
    temperature = models.FloatField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.city} - {self.date}"