# Generated by Django 4.2.3 on 2023-09-22 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0017_forworkerdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='forworkerdata',
            name='priority',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
