# Generated by Django 2.1.5 on 2019-02-01 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imgfile',
            field=models.FileField(blank=True, null=True, upload_to='posts/'),
        ),
    ]