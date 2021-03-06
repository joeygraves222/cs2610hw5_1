# Generated by Django 2.0.2 on 2018-03-28 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('AuthorName', models.CharField(max_length=50)),
                ('Content', models.CharField(max_length=2000)),
                ('PostedDate', models.DateField(verbose_name='Date Published')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NickName', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Content', models.CharField(max_length=2000)),
                ('PostedDate', models.DateField()),
                ('Blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.BlogPost')),
            ],
        ),
    ]
