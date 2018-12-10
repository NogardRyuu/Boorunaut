# Generated by Django 2.1.2 on 2018-12-09 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booru', '0005_auto_20181206_1852'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_auto_20181120_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostFlag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=32)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booru.Post')),
            ],
            options={
                'verbose_name_plural': 'Post flags',
            },
        ),
    ]
