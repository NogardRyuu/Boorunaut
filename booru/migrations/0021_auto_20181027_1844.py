# Generated by Django 2.1.2 on 2018-10-27 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booru', '0020_auto_20181027_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]