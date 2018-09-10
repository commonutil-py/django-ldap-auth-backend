# -*- coding: utf-8 -*-
""" Setup script of LDAP authentication backend for Django """

from setuptools import setup

setup(
		name="django-ldap-auth-backend",
		version="0.0.3",  # REV-CONSTANT:rev 5d022db7d38f580a850cd995e26a6c2f
		description="LDAP authentication backend for Django",
		packages=[
				"ldapauthbackend",
				"ldapauthbackend.migrations",
		],
		install_requires=[
				"python-ldap ~= 3.1.0",
		])

# vim: ts=4 sw=4 ai nowrap