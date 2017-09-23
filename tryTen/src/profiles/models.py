from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up
# Create your models here.
class profile(models.Model):
	name = models.CharField(max_length=120)
	user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank = True)
	description = models.TextField(default='description default TextField')
	location = models.CharField(max_length=120,default='my location')
	job = models.CharField(max_length=120,default='my location')

	def __unicode__(self):
		return self.name

class userStripe(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	stripe_id = models.CharField(max_length=50, null=True, blank=True)

	def __unicode__(self):
		if self.stripe_id:
			return self.stripe_id
		else:
			return self.user.username

def my_callback(sender,request, user, **kwargs):
    idStripe, created = userStripe.objects.get_or_create(user=user)
    if created:
    	print 'created for %s'%(user.username)

    userProfile, is_created = profile.objects.get_or_create(user=user)	
    if is_created:
    	userProfile.name = user.username
    	userProfile.save()
#from django.core.signals import request_finished
def stripeCallback(sender,request, user, **kwargs):
    idStripe, created = userStripe.objects.get_or_create(user=user)
    if created:
    	print 'created for %s'%(user.username)



user_logged_in.connect(my_callback)    