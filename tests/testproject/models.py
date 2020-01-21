from django.db import models


class RelatedResource1(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class RelatedResource2(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    related_resources_1 = models.ManyToManyField(RelatedResource1)

    def __str__(self):
        return self.name


class TestResource(models.Model):
    related_resource_1 = models.ForeignKey(RelatedResource1, on_delete=models.CASCADE)
    related_resource_2 = models.OneToOneField(RelatedResource2, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
