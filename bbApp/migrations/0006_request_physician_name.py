# Generated by Django 4.0.3 on 2022-04-02 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbApp', '0005_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='physician_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
