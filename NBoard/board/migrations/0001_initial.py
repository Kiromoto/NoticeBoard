# Generated by Django 4.1.2 on 2022-10-15 22:07

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
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('uploads', models.FileField(upload_to='uploads/')),
                ('category', models.CharField(choices=[('Tanks', 'Танки'), ('Tanks', 'Хилы'), ('DD', 'ДД'), ('Traders', 'Торговцы'), ('Guildmaster', 'Гилдмастеры'), ('Questgivers', 'Квестгиверы'), ('Blacksmiths', 'Кузнецы'), ('Leatherworkers', 'Кожевники'), ('Potions', 'Зельевары'), ('Spell masters', 'Мастера заклинаний')], default='Tanks', max_length=16)),
                ('dt_create', models.DateTimeField(auto_now_add=True)),
                ('isnew', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('dt_create', models.DateTimeField(auto_now_add=True)),
                ('accept', models.BooleanField(default=None)),
                ('to_ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.ad')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authoruser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ad',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='board.author'),
        ),
    ]
