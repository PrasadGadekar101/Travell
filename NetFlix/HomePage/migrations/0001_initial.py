# Generated by Django 4.0.5 on 2022-08-26 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destinations',
            fields=[
                ('dest_pk', models.AutoField(primary_key=True, serialize=False)),
                ('num_days', models.IntegerField(max_length=2)),
                ('num_price', models.IntegerField()),
                ('mode_of_travel', models.CharField(choices=[('R', 'Road'), ('A', 'Air'), ('W', 'Water')], max_length=1)),
                ('spots_covered', models.TextField(max_length=150)),
            ],
        ),
    ]
