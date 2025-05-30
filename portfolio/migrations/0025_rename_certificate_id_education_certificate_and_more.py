# Generated by Django 5.2 on 2025-05-27 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0024_alter_certification_certificate_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='certificate_id',
            new_name='certificate',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='certificate_id',
            new_name='certificate',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
