# Generated by Django 4.0.3 on 2022-03-16 09:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_post_is_working_post_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='complete',
        ),
        migrations.AddField(
            model_name='post',
            name='iofield',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='level',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
