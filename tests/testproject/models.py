from django.db import models


class RelatedResource1(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)


class RelatedResource2(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    related_resources_1 = models.ManyToManyField(RelatedResource1)


class TestResource(models.Model):
    related_resource_1 = models.ForeignKey(RelatedResource1)
    related_resource_2 = models.OneToOneField(RelatedResource2)
    name = models.CharField(max_length=255)
