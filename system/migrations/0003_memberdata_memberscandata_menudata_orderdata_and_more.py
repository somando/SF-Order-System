# Generated by Django 4.2.3 on 2023-09-13 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_member_memberscan_menu_order_ticketscan_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='memberData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('student_id', models.IntegerField()),
                ('barcode', models.CharField(max_length=15)),
                ('work', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='memberScanData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('name', models.CharField(max_length=50)),
                ('student_id', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='menuData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='orderData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField()),
                ('table_id', models.IntegerField()),
                ('menu_id', models.IntegerField()),
                ('count', models.IntegerField()),
                ('provide', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ticketScanData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_id', models.IntegerField()),
                ('barcode', models.CharField(max_length=15)),
                ('used', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='member',
        ),
        migrations.DeleteModel(
            name='memberScan',
        ),
        migrations.DeleteModel(
            name='menu',
        ),
        migrations.DeleteModel(
            name='order',
        ),
        migrations.DeleteModel(
            name='ticketScan',
        ),
    ]
