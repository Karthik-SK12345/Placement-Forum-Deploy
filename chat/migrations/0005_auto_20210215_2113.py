# Generated by Django 3.1.6 on 2021-02-15 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20210215_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
