# Generated by Django 2.1.5 on 2019-05-31 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deferpayapplication',
            old_name='rent_id',
            new_name='lease_id',
        ),
        migrations.RenameField(
            model_name='paymemt',
            old_name='rent_id',
            new_name='lease_id',
        ),
        migrations.RenameField(
            model_name='refundapplication',
            old_name='rent_id',
            new_name='lease_id',
        ),
    ]
