# Generated by Django 2.2.1 on 2019-06-01 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galleries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auhtor', models.CharField(max_length=200)),
                ('gitrepo', models.CharField(max_length=1000)),
            ],
        ),
    ]
