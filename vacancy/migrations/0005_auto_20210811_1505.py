# Generated by Django 3.2.6 on 2021-08-11 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0004_employee'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name_plural': 'Employee'},
        ),
        migrations.AlterModelOptions(
            name='employer',
            options={'verbose_name_plural': 'Employer'},
        ),
        migrations.AddField(
            model_name='employee',
            name='employer',
            field=models.ManyToManyField(blank=True, to='vacancy.Employer'),
        ),
    ]
