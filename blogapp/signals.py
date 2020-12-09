from django.db.models.signals import pre_init,post_init,pre_save,post_save,pre_delete,post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from Suvidha_Blog.settings import EMAIL_HOST_USER
from .models import User


def mail_to_user(msg,instance):
    subject = msg
    message = ' {} for {}..!!'.format(msg, instance)
    email_from = EMAIL_HOST_USER
    receipt = instance.email
    print('receipt----------->',receipt)
    res = send_mail(subject, message, email_from, receipt)
    print(res)


@receiver(post_save,sender=User)
def post_save_emp(sender, instance,created,**kwargs):
    msg = 'Blog Account Has Been Created {} {}'.format(sender, instance)
    print('sending mail to User:',msg)
    res=mail_to_user(msg,instance)
    print(msg)