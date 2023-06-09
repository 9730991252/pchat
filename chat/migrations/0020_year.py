# Generated by Django 4.1.7 on 2023-03-31 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0019_school_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('added_by', models.CharField(max_length=100)),
                ('added_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
    ]
