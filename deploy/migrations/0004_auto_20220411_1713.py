# Generated by Django 3.2 on 2022-04-11 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0003_auto_20190108_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impex',
            name='exclusive_editor',
            field=models.CharField(choices=[('yes', 'package|yes'), ('no', 'package|no')], default='no', max_length=3, verbose_name='impex|exclusive editor'),
        ),
        migrations.AlterField(
            model_name='impex',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='package',
            name='exclusive_editor',
            field=models.CharField(choices=[('yes', 'package|yes'), ('no', 'package|no')], default='no', max_length=3, verbose_name='package|exclusive editor'),
        ),
        migrations.AlterField(
            model_name='package',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='package',
            name='ignoreperiod',
            field=models.CharField(choices=[('yes', 'package|yes'), ('no', 'package|no')], default='no', max_length=3, verbose_name='package|ignore deploy period'),
        ),
        migrations.AlterField(
            model_name='package',
            name='public',
            field=models.CharField(choices=[('yes', 'package|yes'), ('no', 'package|no')], default='no', max_length=3, verbose_name='package| public package'),
        ),
        migrations.AlterField(
            model_name='packagecondition',
            name='depends',
            field=models.CharField(choices=[('installed', 'installed'), ('notinstalled', 'notinstalled'), ('lower', 'lower'), ('higher', 'higher'), ('system_is', 'operating_system_is'), ('system_not', 'operating_system_not'), ('is_W64_bits', 'is_W64_bits'), ('is_W32_bits', 'is_W32_bits'), ('language_is', 'language_is'), ('hostname_in', 'hostname_in'), ('hostname_not', 'hostname_not'), ('username_in', 'username_in'), ('username_not', 'username_not'), ('ipaddr_in', 'ipaddr_in'), ('ipaddr_not', 'ipaddr_not'), ('isfile', 'isfile'), ('notisfile', 'notisfile'), ('isdir', 'isdir'), ('notisdir', 'notisdir'), ('isfiledir', 'isfiledir'), ('notisfiledir', 'notisfiledir'), ('hashis', 'hashis'), ('hashnot', 'hashnot'), ('exitcodeis', 'exitcodeis'), ('exitcodenot', 'exitcodenot')], default='installed', help_text='packagecondition|depends help text', max_length=12, verbose_name='packagecondition|depends'),
        ),
        migrations.AlterField(
            model_name='packagecondition',
            name='exclusive_editor',
            field=models.CharField(choices=[('yes', 'package|yes'), ('no', 'package|no')], default='no', max_length=3, verbose_name='packagecondition|exclusive editor'),
        ),
        migrations.AlterField(
            model_name='packagecondition',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='packagecondition',
            name='softwarename',
            field=models.CharField(blank=True, default='undefined', help_text='packagecondition|softwarename help text', max_length=500, null=True, verbose_name='packagecondition|softwarename'),
        ),
        migrations.AlterField(
            model_name='packagecondition',
            name='softwareversion',
            field=models.CharField(blank=True, default='undefined', help_text='packagecondition|softwareversion help text', max_length=500, null=True, verbose_name='packagecondition|softwareversion'),
        ),
        migrations.AlterField(
            model_name='packagehistory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='packagehistory',
            name='status',
            field=models.CharField(blank=True, default='Programmed', max_length=500, null=True, verbose_name='packagehistory|status'),
        ),
        migrations.AlterField(
            model_name='packageprofile',
            name='exclusive_editor',
            field=models.CharField(choices=[('yes', 'package|yes'), ('no', 'package|no')], default='no', max_length=3, verbose_name='packageprofile|exclusive editor'),
        ),
        migrations.AlterField(
            model_name='packageprofile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='packagewakeonlan',
            name='exclusive_editor',
            field=models.CharField(choices=[('yes', 'package|yes'), ('no', 'package|no')], default='no', max_length=3, verbose_name='packagewakonelan|exclusive editor'),
        ),
        migrations.AlterField(
            model_name='packagewakeonlan',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='packagewakeonlan',
            name='status',
            field=models.CharField(choices=[('Programmed', 'packagewakeonlan|Programmed'), ('Completed', 'packagewakeonlan|Completed')], default='Programmed', max_length=100, verbose_name='packagewakeonlan|status'),
        ),
        migrations.AlterField(
            model_name='timeprofile',
            name='exclusive_editor',
            field=models.CharField(choices=[('yes', 'package|yes'), ('no', 'package|no')], default='no', max_length=3, verbose_name='timeprofile|exclusive editor'),
        ),
        migrations.AlterField(
            model_name='timeprofile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]