# Generated by Django 4.2.6 on 2023-11-28 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0008_alter_book_publication_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('details', models.CharField(max_length=50)),
            ],
        ),
    ]
