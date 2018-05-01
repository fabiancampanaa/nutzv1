# Generated by Django 2.0.4 on 2018-05-01 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('paciente', '0002_auto_20180430_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocupacion', models.CharField(max_length=255)),
                ('nacionalidad', models.CharField(max_length=100)),
                ('observacion', models.TextField(max_length=5000)),
                ('ultima_atencion', models.DateTimeField(blank=True, null=True)),
                ('peso', models.IntegerField(default=0)),
                ('glicemia_mgdl', models.FloatField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
