# Generated by Django 3.0.5 on 2024-05-21 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0003_alter_participant_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
