# Generated by Django 3.2.16 on 2022-12-05 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_customer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(default='uploads/profile_pic.jpg', upload_to='profile_pics/%Y%m%d'),
        ),
    ]
