# Generated by Django 3.0.1 on 2020-02-29 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', null=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='modified_at', null=True, verbose_name='Updated at')),
                ('created_by', models.CharField(blank=True, db_column='created_by', default='', max_length=100, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, db_column='modified_by', default='', max_length=100, null=True, verbose_name='Updated by')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Project Picture Name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Project Image')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Project Picture Description')),
                ('avatar', models.BooleanField(default=False, verbose_name="Project's avatar")),
            ],
            options={
                'verbose_name': 'Project Picture',
                'verbose_name_plural': 'Project Pictures',
            },
        ),
        migrations.CreateModel(
            name='ProjectStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', null=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='modified_at', null=True, verbose_name='Updated at')),
                ('created_by', models.CharField(blank=True, db_column='created_by', default='', max_length=100, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, db_column='modified_by', default='', max_length=100, null=True, verbose_name='Updated by')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Project Style Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Project Style Description')),
                ('juridical', models.CharField(blank=True, max_length=255, null=True, verbose_name='Project Style Juridical')),
            ],
            options={
                'verbose_name': 'Project Style',
                'verbose_name_plural': 'Project Styles',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', null=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='modified_at', null=True, verbose_name='Updated at')),
                ('created_by', models.CharField(blank=True, db_column='created_by', default='', max_length=100, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, db_column='modified_by', default='', max_length=100, null=True, verbose_name='Updated by')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Project Name')),
                ('name_slug', models.SlugField(blank=True, max_length=280, null=True, verbose_name='Project Slug Name')),
                ('owner', models.CharField(blank=True, max_length=255, null=True, verbose_name='Project Owner')),
                ('project_area', models.IntegerField(blank=True, default=0, null=True, verbose_name='Project Area')),
                ('master_plan', models.IntegerField(blank=True, default=0, null=True, verbose_name='Project Master Plan')),
                ('density_of_building', models.IntegerField(blank=True, default=0, null=True, verbose_name='Density Of Building')),
                ('commencement_date', models.DateTimeField(blank=True, null=True, verbose_name='Commencement Date')),
                ('completion_date', models.DateTimeField(blank=True, null=True, verbose_name='Completion Date')),
                ('inspection', models.BooleanField(blank=True, default=False, null=True, verbose_name='Inspection')),
                ('handing_over', models.BooleanField(blank=True, default=False, null=True, verbose_name='Handing Over')),
                ('project_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp_system.ProjectPicture', verbose_name='Project Picture')),
                ('project_style', models.ManyToManyField(blank=True, to='erp_system.ProjectStyle', verbose_name='Project Style')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Project',
            },
        ),
    ]
