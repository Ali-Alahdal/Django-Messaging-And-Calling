# Generated by Django 4.2.16 on 2024-11-30 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("messaging", "0010_chats_chat_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chats",
            name="chat_name",
            field=models.CharField(max_length=225, null=True),
        ),
    ]
