# Generated by Django 4.1.1 on 2022-09-16 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_shopitem_itemimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cartImage', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
