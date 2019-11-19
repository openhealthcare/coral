# Generated by Django 2.0.13 on 2019-11-19 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillingItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('commission', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
