from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from .models import Ad
from celery import shared_task


@shared_task
def everyday_mails():
    try:
        new_ads = []
        recipient_email_list = []
        for ad in Ad.objects.all():
            if ad.isnew:
                new_ads.append({ad: f'http://127.0.0.1:8000{ad.get_absolute_url()}'})
        for user in User.objects.all():
            if user.email:
                recipient_email_list.append(user.email)

    except Exception as e:
        print(f'Ошибка получения новых объявлений. {e}')
    else:
        if new_ads and recipient_email_list:
            subject = f'Опубликованы новые объявления на фанатском сервере одной известной MMORPG'
            html_content = render_to_string('send_everyday.html', {'new_ads': new_ads, })
            msg = EmailMultiAlternatives(subject=subject,
                                         from_email=settings.EMAIL_HOST_USER,
                                         to=recipient_email_list,
                                         )

            msg.attach_alternative(html_content, 'text/html')
            msg.send()

            for one in new_ads:
                for key, value in one.items():
                    key.isnew = False
                    key.save()
