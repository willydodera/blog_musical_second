# Generated by Django 4.0.5 on 2022-08-05 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog_app.image'),
        ),
    ]
