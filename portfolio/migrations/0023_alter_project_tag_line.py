# Generated by Django 5.2 on 2025-05-25 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0022_project_tag_line'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tag_line',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
