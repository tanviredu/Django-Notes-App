# Generated by Django 2.0.3 on 2018-04-06 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0002_auto_20180330_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='img',
            field=models.ImageField(default='', upload_to='notes-img'),
            preserve_default=False,
        ),
    ]
