# Generated by Django 2.0.13 on 2019-05-05 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_uploadfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file_path',
            field=models.FileField(upload_to='media/upload/', verbose_name='上传文件路径'),
        ),
    ]
