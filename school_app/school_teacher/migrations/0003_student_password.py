# Generated by Django 5.1.3 on 2024-11-13 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_teacher', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default='12345', max_length=30),
        ),
    ]
