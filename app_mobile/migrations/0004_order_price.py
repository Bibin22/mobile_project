# Generated by Django 3.1.7 on 2021-03-20 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_mobile', '0003_auto_20210320_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]