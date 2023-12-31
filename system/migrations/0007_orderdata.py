# Generated by Django 4.2.3 on 2023-09-13 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0006_delete_orderdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField()),
                ('table_id', models.IntegerField()),
                ('menu_id', models.IntegerField()),
                ('count', models.IntegerField()),
                ('provide', models.BooleanField()),
                ('checkout', models.BooleanField()),
            ],
        ),
    ]
