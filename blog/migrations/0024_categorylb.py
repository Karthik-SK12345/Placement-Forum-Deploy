# Generated by Django 4.0.3 on 2022-04-24 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_postlb_commentlb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorylb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlelb', models.CharField(blank=True, max_length=255, null=True, verbose_name='Titlelb')),
            ],
        ),
    ]
