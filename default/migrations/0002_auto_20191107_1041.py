# Generated by Django 2.2.5 on 2019-11-07 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='poll_io',
            new_name='poll_id',
        ),
        migrations.AlterField(
            model_name='poll',
            name='subject',
            field=models.CharField(max_length=200, verbose_name='投票主題'),
        ),
    ]
