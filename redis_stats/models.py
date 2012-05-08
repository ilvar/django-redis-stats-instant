from django.db import models
from django.utils.translation import ugettext as _

class RedisStats(models.Model):
    class Meta:
        abstract = True

        @property
        def verbose_name(self):
            return _('Redis stats')

        @property
        def verbose_name_plural(self):
            return self.verbose_name()


