# Generated by Django 4.0.3 on 2022-03-16 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_gallery_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'gallery', 'verbose_name_plural': 'gallery'},
        ),
        migrations.AlterField(
            model_name='gallery',
            name='img',
            field=models.ImageField(upload_to='gallery1/'),
        ),
    ]