# Generated by Django 4.0.3 on 2022-03-16 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_gallery_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.CharField(max_length=128, null=True),
        ),
    ]