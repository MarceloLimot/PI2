# Generated by Django 4.0.4 on 2022-06-26 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_loginprestador_delete_loginfunc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginprestador',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
