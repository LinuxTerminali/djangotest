from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class AddCompanies(models.Model):
    """
    Created new company
    """
    name = models.CharField(max_length=100, default='')
    description = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return self.name


def create_company(sender, **kwargs):
    if kwargs['created']:
        user_profile = AddCompanies.objects.create(name=kwargs['instance'])


class Invitation(models.Model):
    """
    Stores a invitations and status, sent by company admin
    to join their company
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    invitedby = models.ForeignKey(
        User, default=17, on_delete=models.CASCADE, related_name='invitedby')
    text = models.CharField(max_length=100, default='')
    status = models.CharField(max_length=50, default='')
    objects = models.Manager()

    def __str__(self):
        return self.user.username


class UserProfile(models.Model):
    """
    Stores a custom fields for user profile
    autogenerate in the begning with defaults
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(
        AddCompanies, on_delete=models.CASCADE, blank=True, null=True, default='')
    admin = models.BooleanField(default=False)
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    objects = models.Manager()

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    """
    Uses django signals to trigger auto generation of
    custom user fields 
    """
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
# post_save.connect(create_company, sender=UserProfile)
