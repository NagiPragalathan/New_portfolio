# Generated by Django 4.0.1 on 2022-12-18 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='resume',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='skill',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='skill',
            name='language',
            field=models.CharField(max_length=50),
        ),
    ]