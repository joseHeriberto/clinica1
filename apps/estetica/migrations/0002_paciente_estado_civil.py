# Generated by Django 2.2.6 on 2019-10-19 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estetica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='estado_civil',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Estado civil'),
        ),
    ]
