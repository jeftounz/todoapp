from django.db import models
from timezone_field import TimeZoneField
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    timezone = TimeZoneField(default='America/Caracas')  # Campo para la zona horaria
    
    def local_time(self):
        """Devuelve la fecha/hora localizada según la zona horaria guardada"""
        return timezone.localtime(self.date, timezone=self.timezone)
    
    def __str__(self):
        return self.title