# Generated by Django 4.2.16 on 2024-11-25 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("messaging", "0003_chats_username_1_chats_username_2"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="chats",
            unique_together=set(),
        ),
        migrations.AddField(
            model_name="chats",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="chats",
            name="participants",
            field=models.ManyToManyField(
                related_name="Chats", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="messages",
            name="chat",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="chat_messages",
                to="messaging.chats",
            ),
        ),
        migrations.RemoveField(
            model_name="chats",
            name="user_1",
        ),
        migrations.RemoveField(
            model_name="chats",
            name="user_2",
        ),
        migrations.RemoveField(
            model_name="chats",
            name="username_1",
        ),
        migrations.RemoveField(
            model_name="chats",
            name="username_2",
        ),
    ]
