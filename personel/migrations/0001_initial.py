# Generated by Django 2.2.4 on 2019-08-09 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import personel.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('is_suspended', models.BooleanField(default=False)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=personel.models.upload_location)),
                ('invited_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='invited_personels', to=settings.AUTH_USER_MODEL)),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Master')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modified_personels', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonelPlant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('personel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personel.Personel')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plant.Plant')),
            ],
        ),
        migrations.AddField(
            model_name='personel',
            name='plants',
            field=models.ManyToManyField(through='personel.PersonelPlant', to='plant.Plant'),
        ),
        migrations.AddField(
            model_name='personel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='personels', to=settings.AUTH_USER_MODEL),
        ),
    ]
