# Generated by Django 5.2.2 on 2025-06-05 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_spot', '0006_remove_project_hierarchy_remove_project_in_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='resume_des',
            field=models.TextField(blank=True, null=True),
        ),
    ]
