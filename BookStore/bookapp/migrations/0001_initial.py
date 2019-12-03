# Generated by Django 2.2.1 on 2019-05-10 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('copies', models.IntegerField(null=True)),
                ('rackno', models.IntegerField(null=True)),
            ],
        ),
    ]
