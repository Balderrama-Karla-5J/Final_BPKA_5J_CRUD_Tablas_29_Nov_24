# Generated by Django 5.1.2 on 2024-11-19 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id_libro', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=50)),
                ('ilustrador', models.CharField(max_length=50)),
                ('año', models.DateField()),
                ('precio', models.FloatField()),
                ('stock', models.PositiveIntegerField()),
            ],
        ),
    ]
