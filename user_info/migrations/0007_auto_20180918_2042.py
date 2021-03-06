# Generated by Django 2.1 on 2018-09-18 12:42

from django.db import migrations, models
import django.utils.translation


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0006_auto_20180917_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('cost_time', models.IntegerField()),
                ('place', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('theme', models.CharField(max_length=100)),
                ('theme_content', models.CharField(max_length=300)),
                ('remark', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Metting_Record',
        ),
        migrations.AlterField(
            model_name='user',
            name='real_name',
            field=models.CharField(blank=True, max_length=30, verbose_name=django.utils.translation.gettext),
        ),
    ]
