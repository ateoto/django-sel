from django.db import models
from django.template.defaultfilters import slugify

from taggit.managers import TaggableManager


class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    slug_name = models.SlugField()
    tags = TaggableManager()

    class Meta:
        app_label = 'sel'

    def __unicode__(self):
        return "%s" % (self.name)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug_name = slugify(self.name)

        super(Ingredient, self).save(*args, **kwargs)
