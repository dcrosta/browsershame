from django.db import models
from django.contrib import admin

# Create your models here.
class Browser(models.Model):
    name = models.CharField(max_length=255, blank=False)
    major = models.PositiveIntegerField()
    minor = models.PositiveIntegerField(blank=True, null=True)
    tick = models.PositiveIntegerField(blank=True, null=True)

    def __unicode__(self):
        return '%s %s' % (self.name, self.version_number)

    @property
    def version_number(self):
        vers = str(self.major)
        if self.minor is not None:
            vers += '.' + str(self.minor)
            if self.tick is not None:
                vers += '.' + str(self.tick)
        return vers

class Sample(models.Model):
    browser = models.ForeignKey(Browser, db_index=True, related_name='samples')

    cpu = models.IntegerField() # percent
    mem = models.IntegerField() # kilobytes
    tabs = models.IntegerField(blank=True)

    sample_time = models.DateTimeField()

admin.site.register(Browser)
admin.site.register(Sample)
