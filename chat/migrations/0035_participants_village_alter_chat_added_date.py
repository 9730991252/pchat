# Generated by Django 4.1.7 on 2023-04-01 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0034_my_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='participants',
            name='village',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='chat.group_names'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='added_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
