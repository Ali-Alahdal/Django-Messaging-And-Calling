from django.db import models

# Create your models here.
class Test_1(models.Model):
    msg = models.TextField()
    sent_time = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
     
    