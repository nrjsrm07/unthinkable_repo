# Generated by Django 4.2.3 on 2023-08-01 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('profession', models.CharField(max_length=100)),
                ('is_online', models.BooleanField(default=False)),
            ],
        ),
    ]
