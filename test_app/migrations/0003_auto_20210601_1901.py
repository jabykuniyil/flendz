# Generated by Django 3.2.3 on 2021-06-01 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_mark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
