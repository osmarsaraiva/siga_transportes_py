# Generated by Django 5.0.7 on 2024-07-24 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlanoConta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conta', models.IntegerField()),
                ('tipo', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=20)),
                ('subconta', models.IntegerField()),
                ('sigla_situacao', models.CharField(max_length=1)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=11)),
            ],
        ),
    ]
