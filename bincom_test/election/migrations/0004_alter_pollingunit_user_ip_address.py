# Generated by Django 4.2.10 on 2024-02-12 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0003_alter_pollingunit_entered_by_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollingunit',
            name='user_ip_address',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
