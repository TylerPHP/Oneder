# Generated by Django 3.0.8 on 2020-07-17 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clock',
            name='rang',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='clock',
            name='time',
            field=models.DateTimeField(default='2020-07-17 18:33:40', max_length=140),
        ),
    ]