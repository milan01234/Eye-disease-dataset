# Generated by Django 4.1.8 on 2023-05-12 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Eye_Image',
            field=models.FileField(upload_to=''),
        ),
    ]
