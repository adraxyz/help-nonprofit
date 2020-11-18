from django.db import models
from django.utils.translation import ugettext_lazy as _

TOPIC_CHOICES = [
    ("contact_form", _("Contact form")),
    ("shipment_form", _("Shipment form")),
    ("shopping_cart", _("Shopping cart")),
    ("shop_item", _("Shop item"))
]
ITEM_CHOICES = [
    ("first_name", _("First name")),
    ("last_name", _("Last name")),
    ("email", _("email")),
    ("where_from", _("Where from")),
    ("country", _("Country")),
    ("province", _("Province")),
    ("city", _("City")),
    ("address", _("Address")),
    ("address_number", _("Address number")),
    ("cap", _("Postal code")),
    ("phone", _("Phone number")),
    ("age", _("Age")),
    ("object", _("Object")),
    ("message", _("Message")),
    ("news_agreement", _("Agreement to receive the newsletters")),
    ("privacy_agreement", _("Agreement to the privacy policy")),
    ("submit", _("Submit button")),
    ("clear", _("Clear form")),
    ("title", _("Title")),
    ("purchase_order", _("Purchase order")),
    ("reset_cart", _("Reset cart")),
    ("minimum_donation", _("Minimum donation")),
    ("continue", _("Continue")),
    ("shipping_fees", _("Shipping fees")),
    ("total_price", _("Total price")),
    ("summary", _("Summary")),
    ("available", _("Available on"))
]


class Message(models.Model):
    text = models.CharField(
        max_length=250, null=False, blank=False,
        help_text=_("Message text content.")
    )
    topic = models.CharField(
        max_length=50, null=True, blank=True, choices=TOPIC_CHOICES,
        help_text=_("The message field of application (topic).")
    )
    text_to_users = models.CharField(
        max_length=250, null=True, blank=True,
        help_text=_("Message text exposed to users.")
    )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.text_to_users:
            self.text_to_users = self.text
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        s = self.text
        if self.topic:
            s = f"{self.topic} - {s}"
        if self.text_to_users:
            s = f"{s} - {self.text_to_users}"
        return s


class Label(models.Model):
    topic = models.CharField(
        max_length=50, choices=TOPIC_CHOICES,
        help_text=_("The label field of application (topic).")
    )
    item = models.CharField(
        max_length=100, choices=ITEM_CHOICES,
        help_text=_("The item the label will apply to.")
    )
    label = models.CharField(
        max_length=150,
        help_text=_("The label which will be visible.")
    )

    def __str__(self):
        return f"{self.topic} {self.item} label"


class CookiesCategory(models.Model):
    name = models.CharField(
        max_length=50,
        help_text=_("Cookies category name.")
    )
    title = models.CharField(
        max_length=50,
        help_text=_("Cookies category title.")
    )
    description = models.TextField(
        max_length=750,
        help_text=_("Cookies category description.")
    )

    def __str__(self):
        return f"{self.name} cookies category"


class CookiesProvider(models.Model):
    name = models.CharField(
        max_length=50,
        help_text=_("Cookies provider name.")
    )
    title = models.CharField(
        max_length=50,
        help_text=_("Cookies provider title.")
    )
    description = models.TextField(
        max_length=500,
        help_text=_("Cookies provider description.")
    )
    default = models.BooleanField(
        default=False,
        help_text=_("Are cookies of this provider enabled by default?")
    )
    readonly = models.BooleanField(
        default=False,
        help_text=_("Are cookies of this provider readonly?")
    )
    category = models.ForeignKey(
        to=CookiesCategory, on_delete=models.CASCADE, related_name='cookies_providers',
        help_text="The category to which the provider belongs."
    )

    def __str__(self):
        return f"{self.category} - {self.name} cookies provider"


class Cookie(models.Model):
    name = models.CharField(
        max_length=50,
        help_text=_("Cookie name.")
    )
    title = models.CharField(
        max_length=50, null=True, blank=True,
        help_text=_("Cookie title.")
    )
    purpose = models.TextField(
        max_length=750,
        help_text=_("Cookie purpose.")
    )
    provider = models.ForeignKey(
        to=CookiesProvider, on_delete=models.CASCADE, related_name='cookies',
        help_text="The provider to which the cookie belongs."
    )
    duration = models.CharField(
        max_length=20, null=True, blank=True,
        help_text=_("Cookie duration (es. 1 year, 1 day, 3 months, etc).")
    )

    def __str__(self):
        return f"{self.provider} - {self.name} cookie"
