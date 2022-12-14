from django.db.models.signals import pre_delete, post_delete
from .models import Projects
from django.dispatch import receiver


@receiver(pre_delete, sender=Projects)
def pre_delete_profile(sender, **kwargs):
    print('You are deleting item !')


@receiver(post_delete, sender=Projects)
def post_delete_profile(sender, **kwargs):
    print('You deleted item !')
