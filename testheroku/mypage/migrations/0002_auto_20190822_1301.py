# Generated by Django 2.2.4 on 2019-08-22 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myimage',
            name='image',
            field=models.ImageField(upload_to='myimage/images', verbose_name='Image'),
        ),
    ]
