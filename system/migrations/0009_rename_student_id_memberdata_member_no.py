# Generated by Django 4.2.3 on 2023-09-15 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0008_memberdata_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memberdata',
            old_name='student_id',
            new_name='member_no',
        ),
    ]
