# Generated by Django 4.1.8 on 2023-05-12 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_Name', models.CharField(max_length=50)),
                ('Xender', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Eye_Image', models.ImageField(upload_to='')),
                ('Disease', models.CharField(max_length=50)),
            ],
        ),
    ]
