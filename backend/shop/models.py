from django.db import models
from django.utils.translation import ugettext_lazy as _

SHIPMENT_STATE_CHOICES = [
    ("sent", _("Sent")),
    ("received", _("Received")),
    ("check_required", _("Donation check required")),
    ("incorrect_donation", _("Donation amount not correct")),
    ("checked", _("Donation checked")),
    ("in_progress", _("In progress")),
    ("customer_notified", _("Customer notified")),
    ("executed", _("Executed"))
]

SHOP_SLUG_CHOICES = [
    ("paypal_free_shop", _("paypal free shop"))
]


class ProductCategory(models.Model):
    order = models.PositiveSmallIntegerField(
        help_text=_("Product position in the list.")
    )
    title = models.CharField(
        max_length=50, unique=True,
        help_text=_("Product category title.")
    )
    subtitle = models.CharField(
        max_length=250, null=True, blank=True,
        help_text=_("Product category subtitle.")
    )
    description = models.TextField(
        max_length=1000, null=True, blank=True,
        help_text=_("Product category description (max 1000 characters).")
    )
    icon = models.ImageField(
        null=True, blank=True,
        help_text=_("Product category icon.")
    )
    internal = models.BooleanField(
        default=False,
        help_text=_("Is the category's products salable through the site?")
    )
    active = models.BooleanField(
        default=False,
        help_text=_("Is the category (and all the products that belong to it) visible or not?")
    )

    def __str__(self):
        return f"{self.order} - {self.title}"


class Product(models.Model):
    order = models.PositiveSmallIntegerField(
        help_text=_("Product position in the list.")
    )
    title = models.CharField(
        max_length=150,
        help_text=_("Product title.")
    )
    subtitle = models.CharField(
        max_length=250, null=True, blank=True,
        help_text=_("Product subtitle.")
    )
    description = models.TextField(
        max_length=1000, null=True, blank=True,
        help_text=_("Product description (max 1000 characters).")
    )
    slug = models.SlugField(
        max_length=100, unique=True,
        help_text="A short label used in URLs, so do not introduces white spaces."
    )
    thumbnail = models.ImageField(
        null=True, blank=True,
        help_text=_("A thumbnail image of the product.")
    )
    image_0 = models.ImageField(
        null=True, blank=True,
        help_text=_("The first image of the product.")
    )
    image_1 = models.ImageField(
        null=True, blank=True,
        help_text=_("The second image of the product.")
    )
    image_2 = models.ImageField(
        null=True, blank=True,
        help_text=_("The third image of the product.")
    )
    image_3 = models.ImageField(
        null=True, blank=True,
        help_text=_("The fourth image of the product.")
    )
    image_4 = models.ImageField(
        null=True, blank=True,
        help_text=_("The fifth image of the product.")
    )
    video = models.FileField(
        null=True, blank=True,
        help_text=_("The product video file.")
    )
    price = models.FloatField(
        blank=True, null=True,
        help_text=_("Minimum offer for the product.")
    )
    shop_link = models.CharField(
        max_length=1000, null=True, blank=True,
        help_text=_("ONLY FOR EXTERNAL SHOP! Link to the shop page.")
    )
    availability = models.PositiveSmallIntegerField(
        null=True, blank=True,
        help_text=_("ONLY FOR INTERNAL SHOP! Product available quantity.")
    )
    active = models.BooleanField(
        default=False,
        help_text=_("Is the product visible or not?")
    )
    details_active = models.BooleanField(
        default=False,
        help_text=_("Is the product details visible or not?")
    )
    category = models.ForeignKey(
        to=ProductCategory, on_delete=models.CASCADE, related_name='products', null=True, blank=True,
        help_text=_("Product category.")
    )

    def __str__(self):
        return f"{self.order} - {self.title}"


class Shipment(models.Model):
    email = models.EmailField(
        blank=True, null=True,
        help_text=_("Recipient email address.")
    )
    first_name = models.CharField(
        max_length=50, null=True, blank=True,
        help_text=_("Recipient first name.")
    )
    last_name = models.CharField(
        max_length=50, null=True, blank=True,
        help_text=_("Recipient last name.")
    )
    address = models.CharField(
        max_length=250, null=True, blank=True,
        help_text=_("Recipient address.")
    )
    address_number = models.CharField(
        max_length=10, null=True, blank=True,
        help_text=_("Recipient address number.")
    )
    country = models.CharField(
        max_length=50, null=True, blank=True,
        help_text=_("Recipient country.")
    )
    city = models.CharField(
        max_length=50, null=True, blank=True,
        help_text=_("Recipient city.")
    )
    province = models.CharField(
        max_length=2, null=True, blank=True,
        help_text=_("Recipient province.")
    )
    cap = models.CharField(
        max_length=5, null=True, blank=True,
        help_text=_("Recipient postal code.")
    )
    phone = models.CharField(
        max_length=20, null=True, blank=True,
        help_text=_("Recipient phone number.")
    )
    products = models.TextField(
        max_length=1500, null=True, blank=True,
        help_text=_("Products in the shopping cart.")
    )
    total_price = models.PositiveSmallIntegerField(
        null=True, blank=True,
        help_text=_("Minimum donation.")
    )
    timestamp = models.DateTimeField(
        auto_now=True,
        help_text=_("Ordering timestamp.")
    )
    state = models.CharField(
        max_length=30, null=True, blank=True, choices=SHIPMENT_STATE_CHOICES,
        help_text=_("Shipment state.")
    )

    def __str__(self):
        return f"Shipment  - {self.email} - {self.timestamp}"


class Shop(models.Model):
    slug = models.SlugField(
        max_length=100, unique=True, default="paypal_free_shop", choices=SHOP_SLUG_CHOICES,
        help_text="A short label used in URLs, so do not introduces white spaces."
    )
    payment_link = models.CharField(
        max_length=1000, null=True, blank=True,
        help_text=_("URL of the payment platform.")
    )
    shipping_fees = models.PositiveSmallIntegerField(
        null=True, blank=True,
        help_text=_("Shipping fees.")
    )

    def __str__(self):
        return f"Shop {self.slug}"
