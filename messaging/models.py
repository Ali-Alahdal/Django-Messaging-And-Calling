from django.db import models
from users.models import CustomUser
# Create your models here.
class Chats(models.Model):
    user_1 = models.ForeignKey(CustomUser , on_delete=models.CASCADE , related_name="chat_user1")
    user_2 = models.ForeignKey(CustomUser , on_delete=models.CASCADE  , related_name="chat_user2")
    username_1 = models.CharField(max_length=150)  # Assuming max_length based on typical username length
    username_2 = models.CharField(max_length=150)

    class Meta:
        unique_together = ('user_1', 'user_2')

   


class Messages(models.Model):
    chat = models.ForeignKey(Chats , on_delete=models.CASCADE , related_name="message_chat")
    content = models.TextField()
    sender = models.ForeignKey(CustomUser ,  on_delete=models.CASCADE , related_name="message_sender")
    receiver = models.ForeignKey(CustomUser ,  on_delete=models.CASCADE , related_name="message_receiver")
    send_time = models.DateTimeField(auto_now_add=True)
