# Generated by Django 3.2.12 on 2023-06-24 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='etat',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]