# Generated by Django 4.1.7 on 2023-04-01 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0035_participants_village_alter_chat_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
