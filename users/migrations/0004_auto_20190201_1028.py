# Generated by Django 2.1.5 on 2019-02-01 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_post_imgfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imgfile',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
    ]
