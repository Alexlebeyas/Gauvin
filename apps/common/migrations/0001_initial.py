# Generated by Django 4.2 on 2023-07-26 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(db_column='icLangue', primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='cDescription', max_length=50, null=True)),
                ('description_en', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='cDescriptionAn', max_length=50, null=True)),
            ],
            options={
                'db_table': 'tblLangue',
                'managed': True,
            },
        ),
    ]
