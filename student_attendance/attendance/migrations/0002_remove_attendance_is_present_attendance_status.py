# Generated by Django 5.1.3 on 2024-11-17 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='is_present',
        ),
        migrations.AddField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('present', 'Present'), ('absent', 'Absent')], default='absent', max_length=10),
        ),
    ]