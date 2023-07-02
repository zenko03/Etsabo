# Generated by Django 3.2.12 on 2023-07-02 07:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_collaboration_piece_jointe'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaboration',
            name='date_demande',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collaboration',
            name='date_fin',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='fonctioncollab',
            name='temps',
            field=models.IntegerField(default=6),
            preserve_default=False,
        ),
    ]
