# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class LDAPUserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	dn = models.CharField(max_length=255)
	user_id = models.BigIntegerField(default=-1)
	user_name = models.CharField(max_length=127)
	import_staff = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="+", editable=False)

	def __unicode__(self):
		return "LDAPUserProfile(user=%r, dn=%s, import_staff=%r)" % (
				self.user,
				self.dn,
				self.import_staff,
		)
