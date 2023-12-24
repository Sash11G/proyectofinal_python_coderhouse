# accounts/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Avatar
from cliente.models import BlogPost

@receiver(post_save, sender=Avatar)
def update_blog_post_avatar(sender, instance, **kwargs):
    # instance is the Avatar object that was just saved
    user = instance.user
    blog_posts = BlogPost.objects.filter(autor=user)
    for post in blog_posts:
        post.avatar = instance
        post.save()
