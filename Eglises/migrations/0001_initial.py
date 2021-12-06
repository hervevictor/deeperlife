# Generated by Django 3.2.4 on 2021-11-16 13:43

import ckeditor.fields
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
            name='Districts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nom_du_pasteur_du_district', models.CharField(max_length=100)),
                ('nom_du_pasteur_du_superviseur', models.CharField(max_length=100)),
                ('nom_du_pasteur_du_superviseur_ajoin', models.CharField(max_length=100)),
                ('nom_du_pasteur_du_groupe', models.CharField(max_length=100)),
                ('add_date', models.DateField(auto_now_add=True)),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_du_jeune', models.CharField(max_length=200)),
                ('projects', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('add_date', models.DateField(auto_now_add=True)),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('district_du_jeune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eglises.districts')),
            ],
        ),
        migrations.CreateModel(
            name='JeunesDifficultes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_du_jeune', models.CharField(max_length=200)),
                ('difficultes', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('add_date', models.DateField(auto_now_add=True)),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('district_du_jeune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eglises.districts')),
            ],
        ),
    ]
