# Generated by Django 2.1.4 on 2019-02-25 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inven_app', '0009_auto_20190111_0841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
