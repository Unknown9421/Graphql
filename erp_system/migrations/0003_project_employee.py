# Generated by Django 3.0.1 on 2020-02-29 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp_system', '0002_project_projectpicture_projectstyle'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='employee',
            field=models.ManyToManyField(blank=True, to='erp_system.Employee', verbose_name='Project Employee'),
        ),
    ]
