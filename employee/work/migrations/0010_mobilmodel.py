# Generated by Django 4.2.6 on 2023-11-30 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0009_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='mobilModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('details', models.CharField(max_length=30)),
            ],
        ),
    ]
