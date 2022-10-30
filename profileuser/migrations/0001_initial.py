# Generated by Django 4.1 on 2022-10-27 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('email', models.TextField()),
                ('phone', models.TextField()),
                ('mobile', models.TextField()),
                ('address', models.TextField()),
                ('finish', models.BooleanField(default=False)),
            ],
        ),
    ]
