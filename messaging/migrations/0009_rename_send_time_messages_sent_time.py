# Generated by Django 4.2.16 on 2024-11-27 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("messaging", "0008_remove_messages_receiver"),
    ]

    operations = [
        migrations.RenameField(
            model_name="messages",
            old_name="send_time",
            new_name="sent_time",
        ),
    ]
