# Generated by Django 5.0.7 on 2024-07-24 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_message_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='timestamp',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
