# Generated by Django 2.0.4 on 2019-07-03 09:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0033_auto_20190703_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.UUID('3f6d0487-e34f-4f60-920f-34d5e41b8b19'), verbose_name='用户jwt加密秘钥'),
        ),
    ]
