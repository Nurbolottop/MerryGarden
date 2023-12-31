# Generated by Django 4.2.4 on 2023-08-23 08:39

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='team/', verbose_name='Фотография')),
                ('title', models.CharField(max_length=255, verbose_name='Имя')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('whatsapp', models.URLField(blank=True, null=True, verbose_name='Whatspp URL')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram URL')),
                ('youtube', models.URLField(blank=True, null=True, verbose_name='Youtube URL')),
            ],
            options={
                'verbose_name': 'Наша команда',
                'verbose_name_plural': 'Наша команда',
            },
        ),
    ]
