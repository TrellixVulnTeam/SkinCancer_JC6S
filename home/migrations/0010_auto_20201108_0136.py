# Generated by Django 3.0.3 on 2020-11-07 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_filemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkinCancer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idskin', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='path',
            field=models.FilePathField(default='C:\\Users\\Priyash Gupta\\Desktop\\SkinCancerDetection\\media', path='C:\\Users\\Priyash Gupta\\Desktop\\SkinCancerDetection\\media'),
        ),
    ]
