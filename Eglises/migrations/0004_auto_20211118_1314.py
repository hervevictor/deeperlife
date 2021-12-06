# Generated by Django 3.2.4 on 2021-11-18 13:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Eglises', '0003_districts_groupe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concerne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.RenameField(
            model_name='jeunesdifficultes',
            old_name='nom_du_jeune',
            new_name='district_du_concerne',
        ),
        migrations.RenameField(
            model_name='projects',
            old_name='nom_du_jeune',
            new_name='district_du_concerne',
        ),
        migrations.RemoveField(
            model_name='jeunesdifficultes',
            name='district_du_jeune',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='district_du_jeune',
        ),
        migrations.AddField(
            model_name='jeunesdifficultes',
            name='etes_vous',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jeunesdifficultes',
            name='nom_du_concerne',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='etes_vous',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='nom_du_concerne',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
