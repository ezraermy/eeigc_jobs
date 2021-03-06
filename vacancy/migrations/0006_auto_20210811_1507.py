# Generated by Django 3.2.6 on 2021-08-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0005_auto_20210811_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='CoverLetter',
            field=models.FileField(null=True, upload_to='', verbose_name='Cover Letter'),
        ),
        migrations.AddField(
            model_name='employee',
            name='bsc',
            field=models.FileField(null=True, upload_to='', verbose_name='BSc'),
        ),
        migrations.AddField(
            model_name='employee',
            name='msc',
            field=models.FileField(null=True, upload_to='', verbose_name='MSc'),
        ),
        migrations.AddField(
            model_name='employee',
            name='od',
            field=models.FileField(null=True, upload_to='', verbose_name='Other Documents'),
        ),
        migrations.AddField(
            model_name='employee',
            name='phd',
            field=models.FileField(null=True, upload_to='', verbose_name='PhD'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employer',
            field=models.ManyToManyField(blank=True, to='vacancy.Employer'),
        ),
    ]
