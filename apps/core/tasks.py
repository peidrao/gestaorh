from django.core.mail import send_mail

from celery import shared_task


@shared_task
def send_report():
    send_mail(
        'Relatório Celery',
        'Meu relatório aqui',
        'peidrao01@gmail.com',
        ['contatopedrorn@gmail.com'],
        fail_silently=False
    )
