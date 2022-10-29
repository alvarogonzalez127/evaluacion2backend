# Generated by Django 4.1.1 on 2022-10-27 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('fechareserva', models.DateField()),
                ('horareserva', models.TimeField()),
                ('cantidadpersonas', models.IntegerField()),
                ('estado', models.CharField(max_length=25)),
                ('observacion', models.CharField(max_length=255)),
            ],
        ),
    ]
