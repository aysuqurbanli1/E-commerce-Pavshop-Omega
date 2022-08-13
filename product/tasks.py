import time
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from celery import shared_task

from product.models import  ProductVersion, Review
from core.models import Subscription
from django.db.models import Count

import datetime

from product.publisher import Publish



@shared_task
def process_func():
    time.sleep(10)
    return 'Process done'


@shared_task
def send_mail_to_subscribers():
    date = datetime.date.today() + datetime.timedelta(days=1)
    last_week = date - datetime.timedelta(days=7)
    # select email from Subscriber # (('idris',), ('idris'), ('idris'))
    email_list = Subscription.objects.filter(is_active=True).values_list('email', flat=True)
    products = ProductVersion.objects.filter(created_at__range=[last_week, date]).annotate(chapters_cnt=Count('reviews')).order_by('-chapters_cnt')[:3]
    mail_text = render_to_string('email-subscribers.html', {
        'products': products, 
    })    

    # mail_text="salam"
    # Publish(data={"body": mail_text, "subject": "News about site", "recipients": list(email_list), "subtype": "html"  }, event_type="send_mail")
    # celery
    msg = EmailMultiAlternatives(subject='Products', body=mail_text, from_email=settings.EMAIL_HOST_USER, to=email_list, )
    msg.attach_alternative(mail_text, "text/html")
    msg.send()

# 1. background task
# 2. paralel
# 3. periodic task 