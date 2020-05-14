# Generated by Django 3.0.3 on 2020-05-13 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(help_text='Project position in the list.')),
                ('title', models.CharField(help_text='Project category title.', max_length=50, unique=True)),
                ('title_it', models.CharField(help_text='Project category title.', max_length=50, null=True, unique=True)),
                ('title_en', models.CharField(help_text='Project category title.', max_length=50, null=True, unique=True)),
                ('subtitle', models.CharField(blank=True, help_text='Project category subtitle.', max_length=250, null=True)),
                ('subtitle_it', models.CharField(blank=True, help_text='Project category subtitle.', max_length=250, null=True)),
                ('subtitle_en', models.CharField(blank=True, help_text='Project category subtitle.', max_length=250, null=True)),
                ('description', models.TextField(blank=True, help_text='Project category description (max 1000 characters).', max_length=1000, null=True)),
                ('description_it', models.TextField(blank=True, help_text='Project category description (max 1000 characters).', max_length=1000, null=True)),
                ('description_en', models.TextField(blank=True, help_text='Project category description (max 1000 characters).', max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, help_text='A representative image of the project category.', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(help_text='Project position in the list.')),
                ('title', models.CharField(help_text='Project title.', max_length=150)),
                ('title_it', models.CharField(help_text='Project title.', max_length=150, null=True)),
                ('title_en', models.CharField(help_text='Project title.', max_length=150, null=True)),
                ('slug', models.SlugField(help_text='A short label used in URLs, so do not introduces white spaces.', max_length=100, unique=True)),
                ('slug_it', models.SlugField(help_text='A short label used in URLs, so do not introduces white spaces.', max_length=100, null=True, unique=True)),
                ('slug_en', models.SlugField(help_text='A short label used in URLs, so do not introduces white spaces.', max_length=100, null=True, unique=True)),
                ('subtitle', models.CharField(blank=True, help_text='Project subtitle.', max_length=250, null=True)),
                ('subtitle_it', models.CharField(blank=True, help_text='Project subtitle.', max_length=250, null=True)),
                ('subtitle_en', models.CharField(blank=True, help_text='Project subtitle.', max_length=250, null=True)),
                ('description', models.TextField(blank=True, help_text='Project description (max 1000 characters).', max_length=1000, null=True)),
                ('description_it', models.TextField(blank=True, help_text='Project description (max 1000 characters).', max_length=1000, null=True)),
                ('description_en', models.TextField(blank=True, help_text='Project description (max 1000 characters).', max_length=1000, null=True)),
                ('thumbnail', models.ImageField(blank=True, help_text='A thumbnail image of the project.', null=True, upload_to='')),
                ('country', models.CharField(blank=True, help_text='Country where the project takes place.', max_length=50, null=True)),
                ('country_it', models.CharField(blank=True, help_text='Country where the project takes place.', max_length=50, null=True)),
                ('country_en', models.CharField(blank=True, help_text='Country where the project takes place.', max_length=50, null=True)),
                ('region', models.CharField(blank=True, help_text='Region where the project takes place.', max_length=50, null=True)),
                ('region_it', models.CharField(blank=True, help_text='Region where the project takes place.', max_length=50, null=True)),
                ('region_en', models.CharField(blank=True, help_text='Region where the project takes place.', max_length=50, null=True)),
                ('city', models.CharField(blank=True, help_text='City where the project takes place.', max_length=50, null=True)),
                ('city_it', models.CharField(blank=True, help_text='City where the project takes place.', max_length=50, null=True)),
                ('city_en', models.CharField(blank=True, help_text='City where the project takes place.', max_length=50, null=True)),
                ('address', models.CharField(blank=True, help_text='Address where the project takes place.', max_length=250, null=True)),
                ('address_it', models.CharField(blank=True, help_text='Address where the project takes place.', max_length=250, null=True)),
                ('address_en', models.CharField(blank=True, help_text='Address where the project takes place.', max_length=250, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=16, help_text='Place latitude.', max_digits=22, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=16, help_text='Place longitude.', max_digits=22, null=True)),
                ('budget', models.FloatField(blank=True, help_text='Project budget.', null=True)),
                ('category', models.ForeignKey(blank=True, help_text='Project category.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='projects.ProjectCategory')),
            ],
        ),
    ]