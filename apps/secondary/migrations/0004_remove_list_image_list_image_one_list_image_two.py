# Generated by Django 4.2.4 on 2023-09-13 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0003_list_alter_gallery_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='image',
        ),
        migrations.AddField(
            model_name='list',
            name='image_one',
            field=models.ImageField(default=1, upload_to='gallery_image', verbose_name='Первая фотография'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='list',
            name='image_two',
            field=models.ImageField(default=1, upload_to='gallery_image', verbose_name='Вторая фотография'),
            preserve_default=False,
        ),
    ]
