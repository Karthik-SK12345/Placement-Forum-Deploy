# Generated by Django 4.0.3 on 2022-03-29 13:07

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0015_remove_post_explanation_remove_post_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorycpp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='Postcpp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('category', models.CharField(default='coding', max_length=255)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('level', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('link', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('topics', models.CharField(default='sample', max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='blogpostcpp', to=settings.AUTH_USER_MODEL)),
                ('saves', models.ManyToManyField(blank=True, related_name='blogsavecpp', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
