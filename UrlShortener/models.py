from django.db import models
from django.core.validators import URLValidator
import uuid


# Create your models here.


class Url(models.Model):
	actual = models.URLField()
	short = models.UUIDField(default=uuid.uuid4, editable=False)


