# Generated by Django 3.2.4 on 2021-10-14 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tilte', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Produts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tilte', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField(max_length=200)),
                ('imag', models.ImageField(blank=True, null=True, upload_to='images')),
                ('price_sell', models.FloatField(default=False)),
                ('time_see', models.TimeField(auto_now=True)),
                ('date_publ', models.DateTimeField()),
                ('category', models.ManyToManyField(to='blog.Category')),
            ],
        ),
    ]
