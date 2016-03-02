from django.db import models
from django.core.validators import URLValidator


# Create your models here.


class UrlField(models.Model):
	field = models.TextField(Validators=[URLValidator()])
