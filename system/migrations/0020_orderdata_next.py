# Generated by Django 4.2.5 on 2023-09-26 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0019_tabledata_discount_tabledata_ticket_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdata',
            name='next',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
