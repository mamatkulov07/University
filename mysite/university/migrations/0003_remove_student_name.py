# Generated by Django 5.0.6 on 2024-06-29 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_student_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
    ]
