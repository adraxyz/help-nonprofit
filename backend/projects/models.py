from django.db import models
from django.utils.translation import ugettext_lazy as _


class ProjectCategory(models.Model):
    order = models.PositiveSmallIntegerField(
        help_text=_("Project position in the list.")
    )
    title = models.CharField(
        max_length=50, unique=True,
        help_text=_("Project category title.")
    )
    subtitle = models.CharField(
        max_length=250, null=True, blank=True,
        help_text=_("Project category subtitle.")
    )
    description = models.TextField(
        max_length=1000, null=True, blank=True,
        help_text=_("Project category description (max 1000 characters).")
    )
    image = models.ImageField(
        null=True, blank=True,
        help_text=_("A representative image of the project category.")
    )

    def __str__(self):
        return self.title


class Project(models.Model):
    order = models.PositiveSmallIntegerField(
        help_text=_("Project position in the list.")
    )
    title = models.CharField(
        max_length=150,
        help_text=_("Project title.")
    )
    slug = models.SlugField(
        max_length=100, unique=True,
        help_text="A short label used in URLs, so do not introduces white spaces."
    )
    subtitle = models.CharField(
        max_length=250, null=True, blank=True,
        help_text=_("Project subtitle.")
    )
    description = models.TextField(
        max_length=1000, null=True, blank=True,
        help_text=_("Project description (max 1000 characters).")
    )
    thumbnail = models.ImageField(
        null=True, blank=True,
        help_text=_("A thumbnail image of the project.")
    )
    category = models.ForeignKey(
        to=ProjectCategory, on_delete=models.CASCADE, related_name='projects', null=True, blank=True,
        help_text=_("Project category.")
    )
    country = models.CharField(
        max_length=50, null=True, blank=True,
        help_text=_("Country where the project takes place.")
    )
    region = models.CharField(
        max_length=50, null=True, blank=True,
        help_text=_("Region where the project takes place.")
    )
    city = models.CharField(
        max_length=50, null=True, blank=True,
        help_text=_("City where the project takes place.")
    )
    address = models.CharField(
        max_length=250, null=True, blank=True,
        help_text=_("Address where the project takes place.")
    )
    latitude = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True,
        help_text=_("Place latitude.")
    )
    longitude = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True,
        help_text=_("Place longitude.")
    )
    budget = models.FloatField(
        blank=True, null=True,
        help_text=_("Project budget.")
    )
    # state = models.CharField(
    #     max_length=50, null=True, blank=True,
    #     help_text=_("City where the project takes place.")
    # )

    def __str__(self):
        if self.title:
            return f"{self.title}_project_{self.order}"
        return f"project_{self.order}"
