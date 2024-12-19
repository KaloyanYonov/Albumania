from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Profile

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    superusers_group, _ = Group.objects.get_or_create(name="Superusers")
    staff_group, _ = Group.objects.get_or_create(name="Staff")
    
    content_type = ContentType.objects.get_for_model(Profile)

    all_permissions = Permission.objects.filter(content_type=content_type)
    superusers_group.permissions.set(all_permissions)
    
    limited_permissions = Permission.objects.filter(codename__in=[
        'view_profile', 'change_profile'  
    ])
    staff_group.permissions.set(limited_permissions)
