# Generated by Django 2.1.5 on 2019-05-27 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forlease', '0003_auto_20190527_2233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enterapplication',
            old_name='applicate_date',
            new_name='apply_date',
        ),
        migrations.RenameField(
            model_name='enterapplication',
            old_name='review_date',
            new_name='handle_date',
        ),
        migrations.RenameField(
            model_name='enterapplication',
            old_name='review_status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='unit',
            old_name='loacate',
            new_name='loacation',
        ),
    ]