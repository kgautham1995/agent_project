# Generated by Django 3.0.5 on 2020-09-07 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='agent_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idno', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(max_length=50)),
            ],
        ),
    ]
