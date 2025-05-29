from django.db import models

# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    service_type = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='booking_photos/', blank=True, null=True)
    video = models.FileField(upload_to='booking_videos/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.service_type} on {self.date}"
