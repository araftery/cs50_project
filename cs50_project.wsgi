#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/cs50_project/")

from app import app as application
application.secret_key = 'slf3jh234fsdf'