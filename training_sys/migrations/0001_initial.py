# Generated by Django 3.1.2 on 2020-11-11 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('presentation', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='training_sys.course')),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt', models.CharField(max_length=200)),
                ('comment', models.CharField(blank=True, max_length=40)),
                ('mark', models.DecimalField(blank=True, decimal_places=0, max_digits=3)),
                ('lection', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='training_sys.lection')),
                ('students', models.ManyToManyField(to='training_sys.Student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='training_sys.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(to='training_sys.Teacher'),
        ),
    ]