# Generated by Django 4.0.5 on 2022-07-14 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=13)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
