# Generated by Django 2.1.1 on 2018-09-15 09:19

from django.db import migrations, models
import django.utils.translation


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='real_name',
            field=models.CharField(blank=True, max_length=30, verbose_name=django.utils.translation.gettext),
        ),
    ]