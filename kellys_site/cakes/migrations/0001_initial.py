# Generated by Django 3.0.4 on 2020-04-20 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cakeRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('budget', models.CharField(max_length=200)),
                ('request_date', models.DateTimeField(verbose_name='Date requested: ')),
            ],
        ),
    ]
