# Generated by Django 5.2.2 on 2025-06-05 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_spot', '0004_project_resume_des'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='hierarchy',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='in_resume',
            field=models.BooleanField(default=False),
        ),
    ]
