# Generated by Django 4.1.7 on 2023-03-30 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0015_group_names_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='participants',
            name='village_group',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='chat.group_names'),
        ),
    ]
