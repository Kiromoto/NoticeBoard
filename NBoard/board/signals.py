from django.db.models import signals
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from .models import Response, Ad


@receiver(signals.post_save, sender=Response)
def accept_reject_response(sender, instance, created, **kwargs):
    recipient_email_list = []
    subject = ''
    text = ''
    try:
        ad = Ad.objects.filter(response__ad=instance.ad).distinct()
        ad = ad[0]
        mail_url = f'http://127.0.0.1:8000{ad.get_absolute_url()}'

        if instance.accept:
            subject = f'Ваш отклик ПРИНЯТ!'
            text = f'Ваш отклик {instance.text} на объявление {ad.title} ПРИНЯТ!'
            recipient_email_list.append(instance.user.email)
        elif instance.reject:
            subject = f'Ваш отклик ОТКЛОНЕН!'
            text = f'Ваш отклик {instance.text} на объявление {ad.title} ОТКЛОНЕН!'
            recipient_email_list.append(instance.user.email)
        else:
            subject = 'Ваше объявление получило новый отклик!'
            recipient_email_list.append(ad.author.email)

    except Exception as e:
        print(f'Ошибка получения отклика: {e}')
    else:
        html_content = render_to_string('response_emailsend.html',
                                        {'response': instance, 'ad': ad, 'mail_url': mail_url, })
        msg = EmailMultiAlternatives(subject=subject,
                                     body=text,
                                     from_email=settings.EMAIL_HOST_USER,
                                     to=recipient_email_list,
                                     )

        msg.attach_alternative(html_content, 'text/html')
        msg.send()
    finally:
        print(f'Print from signals.py: {recipient_email_list}')


@receiver(signals.post_delete, sender=Response)
def accept_reject_response(sender, instance, **kwargs):
    recipient_email_list = []
    subject = ''
    text = ''
    try:
        ad = Ad.objects.filter(response__ad=instance.ad).distinct()
        ad = ad[0]
        mail_url = f'http://127.0.0.1:8000{ad.get_absolute_url()}'
        subject = f'Ваш отклик УДАЛЕН!'
        text = f'Ваш отклик {instance.text} на объявление {ad.title} УДАЛЕН!'
        recipient_email_list.append(instance.user.email)

    except Exception as e:
        print(f'Ошибка получения отклика: {e}')
    else:
        html_content = render_to_string('response_emailsend_ondelete.html', {'mail_url': mail_url, })
        msg = EmailMultiAlternatives(subject=subject,
                                     body=text,
                                     from_email=settings.EMAIL_HOST_USER,
                                     to=recipient_email_list,
                                     )

        msg.attach_alternative(html_content, 'text/html')
        msg.send()
    finally:
        print(f'Print from signals.py: {recipient_email_list}')
