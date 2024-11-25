from django.db import models
from users.models import CustomUser
# Create your models here.
class Chats(models.Model):
    participants = models.ManyToManyField(CustomUser , related_name="chats" )
    created_at = models.DateTimeField(auto_now_add=True)
   

   


class Messages(models.Model):
    chat = models.ForeignKey(Chats , on_delete=models.CASCADE , related_name="chat_messages")
    content = models.TextField()
    sender = models.ForeignKey(CustomUser ,  on_delete=models.CASCADE , related_name="message_sender")
    receiver = models.ForeignKey(CustomUser ,  on_delete=models.CASCADE , related_name="message_receiver")
    send_time = models.DateTimeField(auto_now_add=True)
