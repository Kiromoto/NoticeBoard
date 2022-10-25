from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Ad(models.Model):
    TYPE = (
        ('Tanks', 'Танки'),
        ('Hils', 'Хилы'),
        ('DD', 'ДД'),
        ('Traders', 'Торговцы'),
        ('Guildmaster', 'Гилдмастеры'),
        ('Questgivers', 'Квестгиверы'),
        ('Blacksmiths', 'Кузнецы'),
        ('Leatherworkers', 'Кожевники'),
        ('Potions', 'Зельевары'),
        ('Spell masters', 'Мастера заклинаний'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор объявления')
    title = models.CharField(max_length=64, verbose_name='Заголовок объявления')
    text = models.TextField(verbose_name='Текст объявления')
    category = models.CharField(max_length=16, choices=TYPE, default='Tanks', verbose_name='Категория объявления')
    dt_create = models.DateTimeField(auto_now_add=True)
    isnew = models.BooleanField(default=True)
    uploads = models.FileField(upload_to='uploads/', blank=True, verbose_name='Загрузить файл')

    def __str__(self):
        return self.title[:32]

    def get_absolute_url(self):
        return reverse('ad_detail', args=[str(self.id)])

    def get_user_ads(self):
        return self.objects.filter(author=self.reques.user)


class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор отклика')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='Отклик на объявление')
    text = models.TextField(verbose_name='Содержание отклика')
    dt_create = models.DateTimeField(auto_now_add=True)
    accept = models.BooleanField(default=False, blank=True)
    reject = models.BooleanField(default=False, blank=True)

    def get_absolute_url(self):
        return reverse('ad_detail', args=[str(self.ad.id)])

