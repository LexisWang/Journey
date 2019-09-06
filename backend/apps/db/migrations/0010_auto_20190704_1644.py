# Generated by Django 2.0.4 on 2019-07-04 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0009_useraccessmysql'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccessmysql',
            name='mysqlinst',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_access_mysqlinst', to='db.MySQLInst', verbose_name='MYSQL实例id'),
        ),
    ]