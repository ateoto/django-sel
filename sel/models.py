from django.db import models
from django.template.defaultfilters import slugify

from taggit.managers import TaggableManager
from model_utils.managers import InheritanceManager


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
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


class Recipe(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'sel'

    def __unicode__(self):
        return "%s" % (self.name)


class IngredientLine(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredients')
    quantity = models.CharField(max_length=10, default="1")
    measurement = models.CharField(max_length=100, null=True, blank=True)
    preparation = models.CharField(max_length=100, null=True, blank=True)
    objects = InheritanceManager()

    class Meta:
        app_label = 'sel'

    def __unicode__(self):
        return IngredientLine.objects.get_subclass(id=self.id).__unicode__()


class SoloIngredientLine(IngredientLine):
    ingredient = models.ForeignKey(Ingredient)

    class Meta:
        app_label = 'sel'

    def __unicode__(self):
        return "%s %s %s" % (self.ingredient.name, self.quantity, self.measurement)


class RecipeIngredientLine(IngredientLine):
    recipe_ingredient = models.ForeignKey(Recipe)

    class Meta:
        app_label = 'sel'

    def __unicode__(self):
        return "%s %s %s" % (self.recipe.name, self.quantity, self.measurement)
