# Generated by Django 3.2.16 on 2022-12-21 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userPage', '0001_initial'),
        ('alarm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarm',
            name='user_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userPage.userpage'),
        ),
    ]
