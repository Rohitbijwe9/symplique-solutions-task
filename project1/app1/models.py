from django.db import models

# Create your models here.

msg_type=[('SMS','sms'),('MAIL','mail')]

class Reminder(models.Model):
    date=models.DateField()
    time=models.TimeField()
    message=models.TextField()
    reminder_type=models.CharField(max_length=50,choices=msg_type)
