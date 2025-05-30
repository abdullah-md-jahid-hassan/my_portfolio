# Generated by Django 5.2 on 2025-05-16 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_user_options_remove_user_password_user_about_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='banner_image',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio/img/profile_images/'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio/img/project_images/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image_path',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio/img/project_images/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio/img/profile_images/'),
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Certification Title')),
                ('organization', models.CharField(max_length=255, verbose_name='Issuing Organization')),
                ('issue_date', models.DateField(blank=True, null=True, verbose_name='Issue Date')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certifications', to='portfolio.user', verbose_name='User')),
            ],
            options={
                'verbose_name': 'Certification',
                'verbose_name_plural': 'Certifications',
                'ordering': ['-issue_date'],
            },
        ),
    ]
