# Generated by Django 5.2 on 2025-04-21 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authantication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='VLHGuDliG0NL7IElrRcXEVvT67MjBQ3G', editable=False, max_length=32, unique=True),
        ),
    ]
