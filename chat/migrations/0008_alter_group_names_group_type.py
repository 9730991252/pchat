# Generated by Django 4.1.7 on 2023-03-30 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_alter_group_names_group_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_names',
            name='group_type',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='chat.group_type'),
        ),
    ]
