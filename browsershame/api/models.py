from django.db import models
from django.contrib import admin

# Create your models here.
class Browser(models.Model):
    name = models.CharField(max_length=255, blank=False)
    major_version = models.PositiveIntegerField()
    minor_version = models.PositiveIntegerField(blank=True)
    tick_version = models.PositiveIntegerField(blank=True)

    def __unicode__(self):
        return '%s %s' % (self.name, self.version_number)

    @property
    def version_number(self):
        vers = str(self.major_version)
        if self.minor_version is not None:
            vers += '.' + str(self.minor_version)
            if self.tick_version is not None:
                vers += '.' + str(self.tick_version)
        return vers


class Sample(models.Model):
    browser = models.ForeignKey(Browser, db_index=True, related_name='samples')

    cpu = models.IntegerField() # percent
    mem = models.IntegerField() # kilobytes
    tabs = models.IntegerField(blank=True)

    sample_time = models.DateTimeField()

admin.site.register(Browser)
admin.site.register(Sample)
