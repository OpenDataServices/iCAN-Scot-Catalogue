# Generated by Django 2.2.2 on 2019-06-10 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aliss_id', models.UUIDField(unique=True)),
                ('name', models.TextField(blank=True)),
                ('aliss_url', models.TextField(blank=True)),
                ('aliss_permalink', models.TextField(blank=True)),
                ('slug', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('facebook', models.TextField(blank=True)),
                ('twitter', models.TextField(blank=True)),
                ('url', models.TextField(blank=True)),
                ('phone', models.TextField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aliss_id', models.UUIDField(unique=True)),
                ('slug', models.TextField(blank=True)),
                ('aliss_url', models.TextField(blank=True)),
                ('aliss_permalink', models.TextField(blank=True)),
                ('name', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('url', models.TextField(blank=True)),
                ('phone', models.TextField(blank=True)),
                ('email', models.TextField(blank=True)),
                ('active', models.BooleanField()),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalogueapp.Organisation')),
            ],
        ),
    ]