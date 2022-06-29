# Generated by Django 4.0.4 on 2022-06-25 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_remove_login_int'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginFunc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.CharField(blank=True, max_length=16, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('senha', models.CharField(max_length=255)),
                ('nivel', models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], max_length=25)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
