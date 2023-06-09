# Generated by Django 4.1.7 on 2023-04-04 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0041_alter_group_names_ssc_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('added_by', models.CharField(max_length=100)),
                ('added_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='group_names',
            name='hsc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.college'),
        ),
    ]
