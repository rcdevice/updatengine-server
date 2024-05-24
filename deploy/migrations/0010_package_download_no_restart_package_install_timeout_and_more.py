# Generated by Django 4.2.11 on 2024-05-19 14:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0009_alter_packagecondition_depends'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='download_no_restart',
            field=models.CharField(choices=[('-', 'package|unset'), ('yes', 'package|yes'), ('no', 'package|no')], default='-', help_text='deployconfig|download no restart help text', max_length=3, verbose_name='deployconfig|download no restart'),
        ),
        migrations.AddField(
            model_name='package',
            name='install_timeout',
            field=models.PositiveIntegerField(default=600, help_text='deployconfig|install_timeout help text', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3600)], verbose_name='deployconfig|install_timeout'),
        ),
        migrations.AddField(
            model_name='package',
            name='no_break_on_error',
            field=models.CharField(choices=[('-', 'package|unset'), ('yes', 'package|yes'), ('no', 'package|no')], default='-', help_text='deployconfig|no break on error help text', max_length=3, verbose_name='deployconfig|no break on error'),
        ),
    ]